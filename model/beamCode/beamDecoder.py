# Shubham Agarwal, April 2017
# This script dumps the top k results
#  
# 
# To run this script provide data, vocab and output directory path. 
# Run as:

## python beamDecoder.py --beamFile=
# --vocabFile=
# --outputFile=

import numpy as np
import networkx as nx
import cPickle as pickle
import os 
import argparse

parser = argparse.ArgumentParser(
    description="Convert text file to sequence of integers.")
parser.add_argument(
    "--beamFile",
    dest="beamFile",
    type=str,
    help="Beam file path")
parser.add_argument(
    "--vocabFile",
    dest="vocabFile",
    type=str,
    help="Vocab file path")
parser.add_argument(
    "--outputFile",
    dest="outputFile",
    type=str,
    help="output file path")

parser.add_argument(
    "--numDialogue",
    dest="numDialogue",
    type=int,
    help="output file path")

args = parser.parse_args()

data_fn = args.beamFile
vocab_fn =args.vocabFile
output_fn = args.outputFile

def _add_graph_level(graph, level, parent_ids, names, scores):
    """Adds a levelto the passed graph"""
    for i, parent_id in enumerate(parent_ids):
        new_node = (level, i)
        parent_node = (level - 1, parent_id)
        graph.add_node(new_node)
        graph.node[new_node]["name"] = names[i]
        graph.node[new_node]["score"] = str(scores[i])
        graph.node[new_node]["size"] = 100
        # Add an edge to the parent
        graph.add_edge(parent_node, new_node)


def create_graph(predicted_ids, parent_ids, scores, vocab=None):
    def get_node_name(pred):
        return vocab[pred] if vocab else str(pred)
    
    seq_length = predicted_ids.shape[0]
    graph = nx.DiGraph()
    for level in range(seq_length):
        names = [get_node_name(pred) for pred in predicted_ids[level]]
        _add_graph_level(graph, level + 1, parent_ids[level], names, scores[level])
    graph.node[(0, 0)]["name"] = "START"
    return graph


def get_path_to_root(graph, node):
    p = graph.predecessors(node)
    assert len(p) <= 1
    self_seq = [graph.node[node]['name'].split('\t')[0]]
    if len(p) == 0:
        return self_seq
    else:
        return self_seq + get_path_to_root(graph, p[0])


beam_data = np.load(data_fn)
to_dump = []

# Optionally load vocabulary data
vocab = None
if vocab_fn:
    with open(vocab_fn) as file:
        vocab = file.readlines()
    vocab = [_.split('\t')[0] for _ in vocab]
    vocab += ["UNK", "SEQUENCE_START", "SEQUENCE_END"]
    data_len = len(beam_data["predicted_ids"])

# data_iterator = zip(beam_data["predicted_ids"],
#                     beam_data["beam_parent_ids"],
#                     beam_data["scores"])

# for predicted_ids, parent_ids, scores in data_iterator:
print(args.numDialogue)
for idx in range(0,args.numDialogue):
# for idx in range(0,5):
    print idx
    predicted_ids = beam_data["predicted_ids"][idx]
    parent_ids = beam_data["beam_parent_ids"][idx]
    scores = beam_data["scores"][idx]
    
    graph = create_graph(
            predicted_ids=predicted_ids,
            parent_ids=parent_ids,
            scores=scores,
            vocab=vocab)
    
    pred_end_node_names = {pos for pos, d in graph.node.items()
                           if d['name'] == 'SEQUENCE_END'
                           and len(graph.predecessors(pos)) > 0
                           and graph.node[graph.predecessors(pos)[0]]['name'] != 'SEQUENCE_END'}
    
    result = [(tuple(get_path_to_root(graph, pos)[1:-1][::-1]), float(graph.node[pos]['score']))
              for pos in pred_end_node_names]
    
    s_result = sorted(result, key=lambda x: x[1], reverse=True)
    nn_probs = np.exp(np.array(list(zip(*s_result))[1]))
    probs = nn_probs / np.sum(nn_probs)
    result_w_prob = [(path, score, prob) for (path, score), prob in zip(s_result, probs)]
    to_dump.append(np.array(result_w_prob))
nBest = np.array(to_dump)
with open(output_fn, 'wb') as f_out:
    pickle.dump(nBest, f_out)