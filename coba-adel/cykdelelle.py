import os
import re
from str_valid import string_analyzer
from pathlib import Path
import itertools

chomskyGrammar = {}


def loadGrammar(filePath):
    f = open(filePath)
    rules = f.readlines()
    for i in range(len(rules)):
        origin, res = rules[i].split(' -> ')
        options = res.replace(" ", "").removesuffix("\n").split('|')
        for j in range(len(options)):
            value = chomskyGrammar.get(options[j])
            if (value):
                chomskyGrammar[options[j]].append(origin)
            else:
                chomskyGrammar.update({options[j]: [origin]})
    f.close()


def readInputFile(filePath):
    script_location = Path(__file__).absolute().parent
    file_location = script_location/filePath
    f = open(file_location, "r")
    contents = f.read()
    str_valid, contents = string_analyzer(contents)
    if not str_valid:
        return False, contents
    contents = contents.split()
    f.close()

    delimiters = [':', ',', '=', '<', '>', '>=', '<=', '==', '!=', r'\+',
                 '-', r'\*', '/', r'\*\*', r'\(', r'\)', r'\'\'\'', r'\'', r'\"']

    format = r"[A..z]*(" + "|".join(delimiters) + r")[A..z]*"
    contents = [re.split(format, content) for content in contents]
    contents = list(itertools.chain(*contents))
    
    exclude = lambda x: x != ''
    cleaned_contents = list(filter(exclude, contents))

    return True, cleaned_contents


def insertTable(tableSet, rules):
    for rule in rules:
        tableSet.add(rule)


def makeCYKTable(inputText, chomskyGrammar):
    cykTable = [[set() for _ in range(i)]
                for i in range(len(inputText), 0, -1)]

    for i in range(len(inputText)):
        if inputText[i] in chomskyGrammar:
            insertTable(cykTable[0][i], chomskyGrammar[inputText[i]])
        else:
            if re.match(r'[A-z_][A-z0-9_]*', inputText[i]):
                insertTable(cykTable[0][i], chomskyGrammar['variable'])
            if re.match(r'[0-9]*', inputText[i]):
                insertTable(cykTable[0][i], chomskyGrammar['number'])
            if re.match(r'[A-z0-9]*', inputText[i]):
                insertTable(cykTable[0][i], chomskyGrammar['string'])

    for i in range(1, len(inputText)):
        for j in range(len(inputText)-i):
            for k in range(i):
                for p in cykTable[k][j]:
                    for p1 in cykTable[i-k-1][j+k+1]:
                        p2 = p + p1
                        if p2 in chomskyGrammar:
                            insertTable(cykTable[i][j], chomskyGrammar[p2])
    return cykTable


def printCYKTable(cykTable):
    for table in cykTable:
        print(table)


cnfPath = '/cnf.txt'
testPath = '/tesInput.txt'

if __name__ == "__main__":
    workdir = os.curdir
    loadGrammar(workdir + cnfPath)
    inputFile = workdir + testPath
    valid, inputText = readInputFile(inputFile)
    if valid:
        cykTable = makeCYKTable(inputText, chomskyGrammar)
        printCYKTable(cykTable)
    else:
        print(f"String error in line {inputText}")