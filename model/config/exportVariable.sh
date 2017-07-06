source activate virtualEnv

set -e 
export SEQ2SEQ_DIR=
export CODE_DIR=
export PROJECT_HOME=
export DATA_HOME=$PROJECT_HOME/data
export VOCAB_DIR=${DATA_HOME}/Vocab

export VOCAB_SOURCE=$VOCAB_DIR/vocab.source.utf8.noSpecial.txt
export VOCAB_TARGET=$VOCAB_DIR/vocab.target.utf8.noSpecial.txt
export TRAIN_SOURCES=$DATA_HOME/source_train_utf8_noSpecial.txt
export TRAIN_TARGETS=$DATA_HOME/target_train_utf8_noSpecial.txt
export DEV_SOURCES=$DATA_HOME/source_dev_utf8_noSpecial.txt
export DEV_TARGETS=$DATA_HOME/target_dev_utf8_noSpecial.txt
export DEV_TARGETS_REF=$DATA_HOME/target_dev_utf8_noSpecial.txt
export TRAIN_STEPS=4000
export TEST_SOURCES=$DATA_HOME/source_dev_utf8_noSpecial.txt
# Model directory where models are saved
export SAMPLE_CONFIG_DIR=$PROJECT_HOME/models
export MODEL_DIR=$SAMPLE_CONFIG_DIR/enc4dec4/
# Prediction directory where preds are saved
export PRED_DIR=${MODEL_DIR}/pred
export PYTHONIOENCODING=UTF-8

