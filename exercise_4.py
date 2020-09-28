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
