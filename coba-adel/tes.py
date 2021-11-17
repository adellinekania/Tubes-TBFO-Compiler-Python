from itertools import product
from CFGtoCNF import START
import helperAdel
import CFGtoCNF
import re

cnfPath = 'cnf.txt'

chomskyGrammar = {}

def LoadCNF(modelPath):
    file = open(modelPath).read()
    rawRules = file.split('\n')
    print(len(rawRules))
    for i in range (len(rawRules)-1):
        A = rawRules[i].split(' -> ')[0]
        B = rawRules[i].split(' -> ')[1]
        B = B.replace(" ","")
        C = B.split('|')
        for j in range (len(C)):
            value = chomskyGrammar.get(C[j])
            if (value == None):
                chomskyGrammar.update({C[j] : [A]})
            else :
                chomskyGrammar[C[j]].append(A)
    #print(chomskyGrammar)
    # for chom in chomskyGrammar:
    #     print(chomskyGrammar[chom])
    # {'SS': ['S', 'S0'], 'VARA1': ['S', 'S0'], ... }

def readInputFile(filePath) :
    # INi masii rada kurang pas, kayak di print dia jadi ga bisa ngeprint () karena bakal ke split
    # Read from file
    f = open(filePath, "r")
    contents = f.read()
    contents = contents.split()
    f.close()

    result = contents

    operators = [':', ',', '=', '<', '>', '>=', '<=', '==', '!=', r'\+', '-', r'\*', '/', r'\*\*', r'\(', r'\)',r'\'\'\'', r'\'', r'\"']

    # For each operator..
    for operator in operators:
        temporaryResult = []
        # For each statement..
        for statement in result:
            format = r"[A..z]*(" + operator +r")[A..z]*"
            x = re.split(format, statement)
            
            # Append 
            for splitStatement in x:
                temporaryResult.append(splitStatement) 
        result = temporaryResult

    # Strip space
    temporaryResult = []
    for statement in result:
        stripped = statement.split()
        for splitStatement in stripped: 
            temporaryResult.append(splitStatement)

    result = temporaryResult

    # Strip empty string
    result = [string for string in result if string!='']

    return result


def inputToExistCYKVar(inputText):
    for i in range(len(inputText)):
        if inputText[i] not in chomskyGrammar:
            if re.match(r'[A-z_][A-z0-9_]*', inputText[i]):
                inputText[i] = 'variable'
            elif re.match(r'[0-9]*', inputText[i]) :
                inputText[i] = 'number'
            else :
                inputText[i] = 'string'
    return inputText


inputText = readInputFile('tesInput.txt')
print(inputText)
LoadCNF(cnfPath)
inputText = inputToExistCYKVar(inputText)
cykTable = [[[] for j in range(i)] for i in range(len(inputText),0,-1)]



def printCYKTable(cykTable):
    for table in cykTable :
        print(table)

dictt = {
    'AB' : ['S', 'C'],
    'BC' : ['S'],
    'BA' : ['A'],
    'a' : ['C, A'],
    'CC' : ['B'],
    'b' : ['B'],
}
cykTable = []
cykFinal = []
cykTable.append([['B'], ['A', 'C'], ['A', 'C'], ['B'], ['A', 'C']])
cykFinal.append([['B'], ['A', 'C'], ['A', 'C'], ['B'], ['A', 'C']])
cykTable.append([['S', 'A'], ['B'], ['S', 'C'], ['S', 'A']])
cykTable.append([[], ['B'], ['B']])
cykTable.append([[], ['S', 'A', 'C']])
cykTable.append([['S', 'A', 'C']])

#printCYKTable(cykFinal)

# table = []
# for j in range(len(cykTable[0])):  # cykTable[i]
#     tableJ = []
#     for k in range(len(cykTable[0][j]) - 1):
#         for l in range(len(cykTable[0][j+1])):
#             print(cykTable[0][j][k] + cykTable[0][j][l])


