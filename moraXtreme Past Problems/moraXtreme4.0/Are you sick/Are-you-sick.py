def KMP(string, piTables, genes, g):

    n = len(string)

    for x in range(g):
        m = len(genes[x])
        #print(genes[x])
        genes[x] = ' ' + genes[x]
        i = 0
        j = 0
        flag = 0

        while i < n:
            #print(string[i],genes[x][j+1])
            if string[i] == genes[x][j+1]:
                #print(genes[x][j+1])
                #print(string[i],i)
                i += 1
                j += 1
                flag += 1

            else:
                j = piTables[x][j]
                flag = 0
                i += 1

            if flag == m:
                #print(genes[x])
                break

        genes[x] = genes[x].replace(" ","")

        if flag == m:
            print('YES')
            break

    if flag != m:
        print('NO')


def computePi(gene):
    piTable = [0] * (len(gene) + 1)
    j = 0

    i = 1

    while i < len(gene):
        if gene[i] == gene[j]:
            j += 1
            piTable[i] = j
            i += 1

        else:
            if j == 0:
                piTable[i] = 0
                i += 1

            else:
                j = piTable[j - 1]

    return piTable

g = int(input())

genes = []

for _ in range(g):
    str1 = input()
    genes.append(str1)

piTables = []

for gene in genes:
    piTables.append(computePi(gene))


t = int(input())

for _ in range(t):
    str2 = input()
    KMP(str2, piTables, genes, g)
