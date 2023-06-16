#6- Fazer um algoritmo que calcule e escreva o somatório dos valores armazenados numa variável composta unidimensional (vetor) A, de 10 elementos numéricos a serem lidos do dispositivo de entrada.

A = []

# Lendo os números

for i in range (10):
    numero = float(input("Digite um aleatório {}: ".format(i)))
    A.append(numero)

# Somandos os números

soma = sum(A)

#Imprimindo o resultado

print(f"A soma dos 10 valores é {soma}")