# Shubham Agarwal, April 2017
# This script converts file encoding to UTF8
# 
# To run this script provide data and output file path. Also provide fileEncoding 
# Run as:
# python convertEncodingToUTF8.py --dataDirectory='path/to/text/' --outputDirectory='path/to/output'
# Default to 'utf-8' encoding
# Or use --fileEncoding='utf-8' 

import os 
import io
import argparse
## Some lines dont have a full stop. Eg 17 in train
parser = argparse.ArgumentParser(
    description="Convert file encoding to UTF8.")
parser.add_argument(
    "--dataDirectory",
    dest="dataDirectory",
    type=str,
    help="Data directory path")
parser.add_argument(
    "--outputDirectory",
    dest="outputDirectory",
    type=str,
    help="Output directory path")
parser.add_argument(
    "--fileEncoding",
    dest="fileEncoding",
    type=str,
    default='utf-8',
    help="Encoding of file (default to utf-8)" 
)

args = parser.parse_args()

def changeEncoding(readFilePath,writeFilePath,fileType,encoding):
	readFile = open(readFilePath,'r')
	writeFile = io.open(writeFilePath, 'w', encoding=encoding)
	for line in readFile:
		# if fileType == 'source':
		# Now all files are UTF-8 format
		line = line.decode('utf-8')
		# else:
		# 	line = line.decode('latin-1')
		# 	# line = line.decode('ISO-8859-2')
		writeFile.write(line)
	readFile.close()
	writeFile.close()

def encodingWrapper(dataDirectory,outputDirectory,strType,encoding):
	sourceReadFilePath = dataDirectory+'source_'+strType+'.txt'
	targetReadFilePath = dataDirectory+'target_'+strType+'.txt'
	sourceWriteFilePath = outputDirectory+'source_'+strType+'_utf8.txt'
	targetWriteFilePath = outputDirectory+'target_'+strType+'_utf8.txt'
	changeEncoding(sourceReadFilePath,sourceWriteFilePath,'source',encoding)
	changeEncoding(targetReadFilePath,targetWriteFilePath,'target',encoding)

dataDirectory=args.dataDirectory
outputDirectory=args.outputDirectory
encodingWrapper(dataDirectory,outputDirectory,'train',args.fileEncoding)
encodingWrapper(dataDirectory,outputDirectory,'dev',args.fileEncoding)

