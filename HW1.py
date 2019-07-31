import sys
import re
from collections import Counter

def searchWords(textFile):
    textDict={}
    text = re.findall (r'\w+', textFile.read().lower()) 
    textDict = Counter(text)
    for i in sorted(textDict):
        print(f'The word "{i}" is placed in text {str(textDict[i])} time(s)')
        
if len(sys.argv) < 2:
    with open('D:/Automation/Python_trainings/Book.txt') as f: 
        searchWords(f)
else:
    with open(sys.argv[1], 'r') as f:
        searchWords(f)

