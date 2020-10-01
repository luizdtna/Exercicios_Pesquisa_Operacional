

conexoes = {}
for i in range(6):
    conexoes[i] = []
file = open('grafo_question6', 'r')
for i in file:
    i = i.replace('\n','')
    i = i.split(' ')
    no1 = int(i[0])
    no2 = int(i[1])
    conexoes[no1].append(no2)
    conexoes[no2].append(no1)
file.close()

for i, k in conexoes.items():
    print('Vertice: ' + str(i) + ' Tem os adjacentes: '+str(k))