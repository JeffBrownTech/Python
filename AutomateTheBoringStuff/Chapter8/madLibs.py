#! python
# madLibs.py - Reads in text files and prompts user for responses to madlib

import sys, re

if len(sys.argv) == 1:
    print('Please provide a madlib file when calling the program.')
    exit()
elif len(sys.argv) > 2:
    print('Please provide only one madlib file when calling the program.')
    exit()
else:
    filePath = sys.argv[1]

madlibFile = open(filePath)
madLibString = madlibFile.read()
madLibStringArray = madLibString.split(' ')
storyRegex = re.compile(r'(ADJECTIVE|NOUN|ADVERB|VERB)(.)?')
storyReplaceList = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']

for n in range(len(madLibStringArray)):
    if madLibStringArray[n] in storyReplaceList:
        print('Enter an ' + madLibStringArray[n] + ':')

madlibFile.close()