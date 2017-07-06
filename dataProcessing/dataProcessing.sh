export DATA_DIR=/path/to/dir
python convertToParallelText.py --dataDirectory=$DATA_DIR --outputDirectory=$DATA_DIR
python convertEncodingToUTF8.py --dataDirectory=$DATA_DIR --outputDirectory=$DATA_DIR
python removeSpecialCharacters.py --dataDirectory=$DATA_DIR --outputDirectory=$DATA_DIR

source generateCharacterVocab.sh