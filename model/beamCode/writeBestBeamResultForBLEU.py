import numpy as np
import cPickle as pickle
import os 
import argparse
parser = argparse.ArgumentParser(
    description="Dump from pickle to text file")
parser.add_argument(
    "--pickleFilePath",
    dest="pickleFilePath",
    type=str,
    help="Pickle file path")
parser.add_argument(
    "--outputFile",
    dest="outputFile",
    type=str,
    help="outputFile path")
args = parser.parse_args()
outputFilePath = args.outputFile
pickleFilePath = args.pickleFilePath
pickleFile = open(pickleFilePath,'rb')
nBest = pickle.load(pickleFile)
pickleFile.close()
outputFile = open(outputFilePath,'w')
nBest = np.array(nBest)
numDialogue = nBest.shape[0]
for dialogue in range(0,numDialogue):
	predLine = ''.join(nBest[dialogue][0][0])
	outputFile.write(predLine)
	outputFile.write('\n')
outputFile.close()
