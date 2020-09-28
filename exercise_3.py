import random
cont = 0
matriz = []
for i in range(10): #numero de row
    row = []
    for j in range(10):
        row.append(random.randrange(0, 9)) #numero de colunas
    matriz.append(row)

for i in range(0, 10): #numero de row
    for j in range(0, 10): #numero de colunas
        cont += 1
        if cont == 10:
            print(str(matriz[i][j]) + ' ')
            cont = 0
        else:
            print(str(matriz[i][j]) + ' ', end='')

