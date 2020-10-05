# O valor aproximado de uma série com n termos é calculado pelo somatório
# onde i é o número de parcelas do somatório. Faça um programa que solicite ao
# usuário o valor de n e calcule o valor do somatório.

def summation(n, cont = 0, i=1):
   cont += (2*i-1)/(-2)**(i+1)
   if i == n:
       return cont
   else:
       return summation(n, cont, i+1)

n = 10
print(summation(n))