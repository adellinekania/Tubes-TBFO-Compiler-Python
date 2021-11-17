import tes

dictt = {
    'AB' : ['S', 'C'],
    'BC' : ['S'],
    'BA' : ['A'],
    'a' : ['C', 'A'],
    'CC' : ['B'],
    'b' : ['B'],
}

inputText = ['b', 'a', 'a', 'b', 'a']

def makeCYKTable(inputText, chomskyGrammar):
    cykTable = [[[] for j in range(i)] for i in range(len(inputText),0,-1)]

    for i in range(len(inputText)):
        cykTable[0][i] += chomskyGrammar[inputText[i]]

    for i in range(1,len(inputText)):
            for j in range(len(inputText)-i):
                for k in range(i):
                    print(k, j, ' +++ ', (i-k-1), j+k+1)
                    # print(cykTable[k][j], cykTable[i-k-1][j+k+1])
                    for p in cykTable[k][j]:
                        for p1 in cykTable[i-k-1][j+k+1]:
                            p2 = p + p1
                            if p2 in chomskyGrammar:
                                cykTable[i][j] += chomskyGrammar[p2]
                print("AAAAAAAAAAAAAAAAAAAAAAAAAAA")
    return cykTable
