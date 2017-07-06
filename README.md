# sigdialSubmission
Code accompanying SIGdial 2017 submission "A surprisingly effective out-of-the-box char2char model on the E2E NLG Challenge dataset"

## Data Processing
Download the data for the [E2E NLG Challenge](www.macs.hw.ac.uk/InteractionLab/E2E/).  
Run ./dataProcessing/dataProcessing.sh to prepare data in Parallel Text format for the model.
Provide path to data directory before running the bash script

## Running the Model
We have used tf-seq2seq (Google's open source seq2seq framework) for our experiments.

Install the [google/seq2seq](github.com/google/seq2seq/tree/master/seq2seq). 

All the experiments were done for tensorflow 1.0 and a stable version of this library. 

Installation instructions for google seq2seq can be found at the above link. 

To run the model configure model/config/exportVariable.sh:
* virtualEnv (if any)
* SEQ2SEQ_DIR: path to google/seq2seq in your workspace
* CODE_DIR: path to 'model' directory in this cloned repository
* PROJECT_HOME: where the data as well as model would be saved. You would have to create 'data' and 'models' directory in $PROJECT_HOME. Also mkdir $VOCAB_DIR and $MODEL_DIR

To train the model, run model/training/trainSeq2Seq.sh. Configurations used for the model for which we annotated the results are found in nmt_medium.yml

For prediction, run model/prediction/predictionSeq2Seq.sh. Script for using beam search with length penalty have also been provided for reference.  
