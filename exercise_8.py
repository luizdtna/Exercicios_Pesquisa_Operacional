#Usando recursividade, faça um programa que calcule a soma dos valores de um vetor.

x = [1, 2, 3, 4, 5, 6]


def recursion(cont = 0, aux = 0):
    if len(x) == aux:
        return cont
    else:
        cont += x[aux]
        return recursion(cont, aux + 1)


print(recursion())
