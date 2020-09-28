#Faça um programa que leia 2 matrizes de um arquivo .txt de tamanho 10x10 e
#calcule a soma das duas matrizes. Imprima a matriz resultante.

cont = 0
matriz1 = []
matriz2 = []
file1 = open('matriz1','r')
for i in file1:
    i = i.replace("\n", '')
    aux1 = i.split(" ")
    matriz1.append(aux1)

file2 = open('matriz2', 'r')
for i in file2:
    i = i.replace("\n", '')
    aux2 = i.split(" ")
    matriz2.append(aux2)

for i in range(0, 7): #numero de row
    for j in range(0, 10): #numero de colunas
        cont += 1
        if cont == 10: #qtd de itens em cada linha
            soma = int(matriz1[i][j]) + int(matriz2[i][j])
            print(str(soma) + ' ')
            cont = 0
        else:
            soma = int(matriz1[i][j]) + int(matriz2[i][j])
            print(str(soma) + ' ', end='')
