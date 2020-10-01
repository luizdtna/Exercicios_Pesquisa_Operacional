cont = 0
matriz = []
for i in range(6):
    #preenche a matriz com zeros
    row = []
    for j in range(6):
        row.append(0)
    matriz.append(row)

file = open('grafo_question6', 'r')
for f in file:
    f = f.replace('\n', '')
    f = f.split(' ')
    a = int(f[0])#Altera o tipo de string para int
    b = int(f[1])
    c = int(f[2])
    matriz[a][b] = c
    matriz[b][a] = c


for i in range(0, 6): #numero de linhas
    for j in range(0, 6): #numero de colunas
        cont += 1
        if cont == 6:
            print(str(matriz[i][j]))
            cont = 0
        else:
            print(str(matriz[i][j]) + ' ', end='')