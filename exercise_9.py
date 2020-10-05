# Escreva um programa que, para n>0, escreva: ∑ i × ( i+1 )

def summation(n, cont=0, i=1):
    if i > n:
        return cont
    else:
        cont += i * (i + 1)
        return summation(n, cont, i + 1)


n = 50
print(summation(n))
