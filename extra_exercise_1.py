intinerario = [0,3,1,3,3,2,1,0]
custo = 0
cont = 0
matriz = []



file = open('matriz3', 'r')
for i in file:
    i = i.replace('\n','')
    i = i.split(' ')
    matriz.append(i)
file.close()
row_col = len(matriz[0])

print('Matriz')
for i in range(row_col): #numero de linhas
    for j in range(row_col): #numero de colunas
        cont += 1
        if cont == row_col:
            print(str(matriz[i][j]) + ' ')
            cont = 0
        else:
            print(str(matriz[i][j]) + ' ', end='')
print('_______________________________________')


print('O custo do intinerario '+ str(intinerario)+ ' é: ')
for i in range(len(intinerario)):

    if i+1 == len(intinerario): #Critério de parada
        print(' = '+str(custo))
        break
    item_intinerario = matriz[intinerario[i]][intinerario[i + 1]]

    print(item_intinerario, end='')
    custo += int(item_intinerario)

    if i+2 < len(intinerario):
        print(' + ', end='')


