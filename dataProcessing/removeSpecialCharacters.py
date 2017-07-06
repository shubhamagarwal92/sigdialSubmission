import os 
import io
import argparse
import re
## Some lines dont have a full stop. Eg 17 in train
parser = argparse.ArgumentParser(
    description="Remove special characters.")
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
chars = {
    # 'client\xc3\x83\xc2\xa8le' :'clientele',
    # 'Caf\xc3\x83\xc2\xa9':'Caf^',
    # 'Cafe\xc3\x83\xc2\xa9':'Caf^',
    # 'Cafe\xc3\x82\xc2\xa9':'Caf^',
    # 'Caf\xc3\x83\xc2\xa9\xc3\x82\xc2\xa9':'Caf^',
    # 'caf\xc3\x83\xc2\xa9\xc3\x82\xc2\xa9':'caf^',
    # 'caf\xc3\x83\xc2\xa9':'caf^',
    # 'cafe\xc3\x83\xc2\xa9':'caf^',
    # 'cafe\xc3\x82\xc2\xa9':'caf^',
    # 'they\xc3\xa2\xc2\x82\xc2\xac\xc3\xa2\xc2\x84\xc2\xa2re':'they are',
    '\xc3\xa9' :'^',
    '\xc2\xa3' :'$'
    }

def replace_chars(match):
    # print match
    char = match.group(0)
    # print char
    return chars[char]

args = parser.parse_args()

def replaceCharacters(readFilePath,writeFilePath):
    readFile = open(readFilePath,'r')
    writeFile = open(writeFilePath,'w')
    for line in readFile:
        line = re.sub('(' + '|'.join(chars.keys()) + ')', replace_chars, line)
        writeFile.write(line)
    readFile.close()
    writeFile.close()

def replacingWrapper(dataDirectory,outputDirectory,strType):
    sourceReadFilePath = dataDirectory+'source_'+strType+'.txt'
    targetReadFilePath = dataDirectory+'target_'+strType+'.txt'
    sourceWriteFilePath = outputDirectory+'source_'+strType+'_noSpecial.txt'
    targetWriteFilePath = outputDirectory+'target_'+strType+'_noSpecial.txt'
    replaceCharacters(sourceReadFilePath,sourceWriteFilePath)
    replaceCharacters(targetReadFilePath,targetWriteFilePath)

dataDirectory=args.dataDirectory
outputDirectory=args.outputDirectory
replacingWrapper(dataDirectory,outputDirectory,'train_utf8')
replacingWrapper(dataDirectory,outputDirectory,'dev_utf8')
