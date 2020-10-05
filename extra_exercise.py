intinerario = [0,1,2,5,6,8,3,0,2]
custo = 0
cont = 0
matriz = []

file = open('matriz1', 'r')
for i in file:
    i = i.replace('\n','')
    i = i.split(' ')
    matriz.append(i)
file.close()

print('Matriz')
for i in range(0, 10): #numero de linhas
    for j in range(0, 10): #numero de colunas
        cont += 1
        if cont == 10:
            print(str(matriz[i][j]) + ' ')
            cont = 0
        else:
            print(str(matriz[i][j]) + ' ', end='')
print('_______________________________________')


print('O custo do intinerario '+ str(intinerario)+ ' é: ')
for i in range(len(intinerario)):

    if i+1 == len(intinerario):
        print(' = '+str(custo))
        break
    item_intinerario = matriz[intinerario[i]][intinerario[i + 1]]

    print(item_intinerario, end='')
    custo += int(item_intinerario)

    if i+2 < len(intinerario):
        print(' + ', end='')


