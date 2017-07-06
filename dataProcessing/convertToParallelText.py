# Shubham Agarwal, April 2017
# This script converts the data into ParallelTextFormat suitable for tf-seq2seq
#  
# 
# To run this script provide data and output directory path. 
# Run as:
# python convertToParallelText.py --dataDirectory='path/to/text/' --outputDirectory='path/to/output'
# Erroneous newline character at 
# Line 603 in devset.csv

# Line 15766, 32411 in trainset.csv

# Line 30049 in trainset.csv
# Remove them before using this script
import os 
import sys
import argparse


parser = argparse.ArgumentParser(
    description="Convert text file to Parallel Text Format")
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

args = parser.parse_args()
def readAndSeparateSourceTarget(dataFilePath,outputDirectory,strType):
    dataFile = open(dataFilePath,'r')
    source_file_path = outputDirectory+'source'+strType+'.txt'
    target_file_path = outputDirectory+'target'+strType+'.txt'
    sourceFile = open(source_file_path,'w')
    targetFile = open(target_file_path,'w')
    # Read header
    dataFile.readline()
    lineNumber = 1
    for line in dataFile:
        lineNumber +=1
        # print lineNumber
        source,target = line.split('",')
        source=source.strip('" ')
        source=source.strip()
        target=target.strip('\n')
        target=target.strip()
        target=target.strip('"')
        # target=target.strip('" ')
        target=target.strip()
        sourceFile.write(source + '\n')
        targetFile.write(target + '\n')
        print(lineNumber)

trainFilePath = args.dataDirectory + 'trainset.csv'
devFilePath = args.dataDirectory + 'devset.csv'
outputDirectory = args.outputDirectory
readAndSeparateSourceTarget(trainFilePath,outputDirectory,'_train')
readAndSeparateSourceTarget(devFilePath,outputDirectory,'_dev')
