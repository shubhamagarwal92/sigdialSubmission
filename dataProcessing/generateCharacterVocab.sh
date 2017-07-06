export DATA_HOME=/path/to/dir
export VOCAB_DIR=${DATA_HOME}/Vocab
mkdir $VOCAB_DIR

export TRAIN_SOURCES=$DATA_HOME/source_train_utf8_noSpecial.txt
export TRAIN_TARGETS=$DATA_HOME/target_train_utf8_noSpecial.txt
export DEV_SOURCES=$DATA_HOME/source_dev_utf8_noSpecial.txt
export DEV_TARGETS=$DATA_HOME/target_dev_utf8_noSpecial.txt
export VOCAB_SOURCE=$VOCAB_DIR/vocab.source.utf8.noSpecial.txt
export VOCAB_TARGET=$VOCAB_DIR/vocab.target.utf8.noSpecial.txt
export VOCAB_SOURCE_DEV=$VOCAB_DIR/vocab.source.dev.utf8.noSpecial.txt
export VOCAB_TARGET_DEV=$VOCAB_DIR/vocab.target.dev.utf8.noSpecial.txt

python generateVocabUTF8.py < $TRAIN_SOURCES  --delimiter='' > $VOCAB_SOURCE
python generateVocabUTF8.py < $TRAIN_TARGETS  --delimiter='' > $VOCAB_TARGET

python generateVocabUTF8.py < $DEV_SOURCES  --delimiter='' > $VOCAB_SOURCE_DEV
python generateVocabUTF8.py < $DEV_TARGETS  --delimiter='' > $VOCAB_TARGET_DEV
