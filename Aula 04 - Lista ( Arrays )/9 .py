#9) Fazer um algoritmo que:

#a) Leia duas variáveis compostas unidimensionais, contendo, cada uma, 25 elementos numéricos;

#b) intercale os elementos desses dois conjuntos formando uma nova variável composta unidimensional de 50 elementos;

#c) Escreva o resultado obtido.

vetor1 = [0] * 25
vetor2 = [0] * 25
vetor_juntos =  [0] * 50

# Ler os valores do primeiro vetor

print("Digite os valores do primeiro vetor:")
for i in range(10):
    vetor1[i] = float(input(f'Digite o valor {i+1}: '))

# Ler os valores do segundo vetor

print("\nDigite os valores do segundo vetor:")
for i in range(10):
    vetor2[i] = float(input(f'Digite o valor {i+1}: '))

# Intercalar os elementos

for i in range(50):
    vetor_juntos[i] = vetor1.append(vetor2)

# Imprimir os vetores

print("\nVetor 1:")
for i in range(25):
    print(vetor1[i])

print("\nVetor 2:")
for i in range(25):
    print(vetor2[i])

print("\nvetor_juntos:")
for i in range(50):
    print(vetor_juntos[i])
