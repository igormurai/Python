#7- Escreva um algoritmo que leia um vetor de 10 valores numéricos reais e os imprima na ordem contrária em que foi lida.

vetor = [0] * 10

# Ler os valores do vetor

for i in range(10):
    vetor[i] = float(input(f'Digite o valor {i+1}: '))

# Imprimir o vetor na ordem contrária

print("Vetor na ordem contrária:")
for i in range(9, -1, -1):
    print(vetor[i])