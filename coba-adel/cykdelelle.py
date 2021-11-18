import re
from pathlib import Path

chomskyGrammar = {}

# LoadCNF sama readInputFile coma copas dari kak mk

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

# INII SALAHHH, gapake
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

# masih duplicate isinya
def makeCYKTable(inputText, chomskyGrammar):
    cykTable = [[[] for j in range(i)] for i in range(len(inputText),0,-1)]

    for i in range(len(inputText)):
        if inputText[i] in chomskyGrammar:
            cykTable[0][i] += chomskyGrammar[inputText[i]]
        else:
            if re.match(r'[A-z_][A-z0-9_]*', inputText[i]):
                cykTable[0][i] += chomskyGrammar['variable']
            if re.match(r'[0-9]*', inputText[i]) :
                cykTable[0][i] += chomskyGrammar['number']
            if re.match(r'[A-z0-9]*', inputText[i]):
                cykTable[0][i] += chomskyGrammar['string']
    
    print(cykTable)

    for i in range(1,len(inputText)):
            for j in range(len(inputText)-i):
                for k in range(i):
                    #print(k, j, ' +++ ', (i-k-1), j+k+1)
                    # print(cykTable[k][j], cykTable[i-k-1][j+k+1])
                    for p in cykTable[k][j]:
                        for p1 in cykTable[i-k-1][j+k+1]:
                            p2 = p + p1
                            #print(p2)
                            if p2 in chomskyGrammar:
                                cykTable[i][j] += chomskyGrammar[p2]
                #print("AAAAAAAAAAAAAAAAAAAAAAAAAAA")
    return cykTable

def printCYKTable(cykTable):
    for table in cykTable :
        print(table)

cnfPath = 'cnf.txt'

LoadCNF(cnfPath)
print(chomskyGrammar)
script_location = Path(__file__).absolute().parent
file_location = script_location/'tesInput.txt'
inputText = readInputFile(file_location)
# inputText = readInputFile('tesInput.txt')
print(inputText)

cykTable = makeCYKTable(inputText, chomskyGrammar)

printCYKTable(cykTable)