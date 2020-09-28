# 4. Faça um programa que leia 10 números e calcule imprima o maior valor, o
# menor valor e a média.

import random
list = []
for i in range(10):
    list.append(random.randrange(0,100))

bigger = list[0]
smaller = list[0]
cont = 0
for i in list:
    if i > bigger:
        bigger = i
    if i < smaller:
        smaller = i
    cont += i
media = cont/10

print('Maior valor:'+str(bigger))
print('Menor valor:'+str(smaller))
print('Media:'+str(media))
