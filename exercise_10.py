#10. Dada as matrizes da questão 3, faça um programa que calcule: ∑ ∑ Aij × Bij

matriz1 = []
matriz2 = []
file1 = open('matriz1', 'r')
for i in file1:
    i = i.replace("\n", '')
    aux1 = i.split(" ")
    matriz1.append(aux1)

file2 = open('matriz2', 'r')
for i in file2:
    i = i.replace("\n", '')
    aux2 = i.split(" ")
    matriz2.append(aux2)

def summation():
    cont = 0
    for i in range(10): #linha
        for j in range(10): #coluna
            m1 = int(matriz1[i][j])
            m2 = int(matriz2[i][j])

            cont += m1 * m2
            print(cont)
    return cont
print(summation())