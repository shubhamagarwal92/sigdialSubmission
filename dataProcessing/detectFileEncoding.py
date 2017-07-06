# Shubham Agarwal, April 2017
# This script detects file encoding
#
# Use :set fileencoding in vim otherwise
# python -c 'import chardet,sys; print chardet.detect(sys.stdin.read())' < source_train.txt
# utf-8
# python -c 'import chardet,sys; print chardet.detect(sys.stdin.read())' < target_train.txt
# latin-1 by vim and ISO-8859-2 (latin-2) by chardet

# Run as:
# python detectFileEncoding.py --dataDirectory='path/to/text/' 

import chardet,sys
import argparse

parser = argparse.ArgumentParser(
    description="Detects file encoding using chardet.")
parser.add_argument(
    "--dataDirectory",
    dest="dataDirectory",
    type=str,
    help="Data directory path")
args = parser.parse_args()
def detectFileEncoding(dataDirectory,strType):
	source_file_path = dataDirectory+'source_'+strType+'.txt'
	target_file_path = dataDirectory+'target_'+strType+'.txt'
	source_file = open(source_file_path,'r')
	target_file = open(target_file_path,'r')
	print "Encoding type for source " +strType + " file" 
	print chardet.detect(source_file.read())

	print "Encoding type for target " +strType + " file" 
	print chardet.detect(target_file.read())

detectFileEncoding(args.dataDirectory,'train')
detectFileEncoding(args.dataDirectory,'dev')

# Encoding type for source train file
# {'confidence': 0.99, 'encoding': 'utf-8'}
# Encoding type for target train file
# {'confidence': 0.8690482511453296, 'encoding': 'ISO-8859-2'}
# Encoding type for source dev file
# {'confidence': 0.99, 'encoding': 'utf-8'}
# Encoding type for target dev file
# {'confidence': 0.8680935022843491, 'encoding': 'ISO-8859-2'}
