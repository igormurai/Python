#12- Escreva um algoritmo que:

#a- leia um conjunto A de 20 elementos a partir de uma unidade de entrada;

#b- calcule e imprima o valor de S, onde:

#S = (A[0] - A[19])^2 + (A[1] - A[18])^2 + ... + (A[9] - A[10])^2


# Definindo o vetor A

A = []

# Lendo os valores e armazenando no vetor A

for i in range(20):
    valor = int(input("Digite um valor: "))
    A.append(valor)

# Calculando o valor de S

S = 0
for i in range(10):
    diferenca = A[i] - A[19 - i]
    S += diferenca ** 2

# Imprimindo o valor de S

print("O valor de S é:", S)
