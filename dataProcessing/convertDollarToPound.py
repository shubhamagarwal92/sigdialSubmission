import os 
import io
import argparse
import re

parser = argparse.ArgumentParser(
    description="Convert dollar back to pound symbol.")
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

# chars = {
#     # '$' :'\xc2\xa3',
#     # 'Cafe':'Caf\xc3\xa9'
#     }

# def replace_chars(match):
# 	char = match.group(0)
# 	return chars[char]

# def replaceCharacters(readFilePath,writeFilePath):
#     readFile = open(readFilePath,'r')
#     writeFile = open(writeFilePath,'w')
#     for line in readFile:
#     	print chars.keys()
#         line = re.sub('(' + '|'.join(chars.keys()) + ')', replace_chars, line)
#         writeFile.write(line)
#     readFile.close()
#     writeFile.close()


def replaceCharacters(readFilePath,writeFilePath):
    readFile = open(readFilePath,'r')
    writeFile = open(writeFilePath,'w')
    for line in readFile:
        line = line.replace('$','\xc2\xa3')
        line = line.replace('Caf^','Caf\xc3\xa9')
        line = line.replace('caf^','caf\xc3\xa9')
        writeFile.write(line)
    readFile.close()
    writeFile.close()

def replacingWrapper(dataDirectory,outputDirectory,strType):
    sourceReadFilePath = dataDirectory+'source_'+strType+'_noSpecial.txt'
    targetReadFilePath = dataDirectory+'target_'+strType+'_noSpecial.txt'
    sourceWriteFilePath = outputDirectory+'source_'+strType+'_WithPound.txt'
    targetWriteFilePath = outputDirectory+'target_'+strType+'_WithPound.txt'
    replaceCharacters(sourceReadFilePath,sourceWriteFilePath)
    replaceCharacters(targetReadFilePath,targetWriteFilePath)

replacingWrapper(args.dataDirectory,args.outputDirectory,'train_utf8')
replacingWrapper(args.dataDirectory,args.outputDirectory,'dev_utf8')
