#2. Faça um programa que leia 10 números e os armazene em um vetor. Imprima o vetor.

vet = []
for i in range(0, 10):
    n = int(input('Digite o '+str(i+1)+'º o número\n'))
    vet.append(n)

print(vet)
