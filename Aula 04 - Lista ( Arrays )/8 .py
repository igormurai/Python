#8- Escreva um algoritmo para fazer a soma de dois vetores de 10 elementos reais lidos do teclado. O primeiro elemento do primeiro vetor deverá ser adicionado ao primeiro elemento do segundo vetor e, o resultado deverá ser acumulado em um terceiro vetor também de 10 elementos. Imprimir os três vetores conforme layout de impressão abaixo:

#VETOR 1: __ __ __ __ __ __ __ __ __ __

#VETOR 2: __ __ __ __ __ __ __ __ __ __

#VETOR 3: __ __ __ __ __ __ __ __ __ __

# Inicializar os vetores com 10 elementos

vetor1 = [0] * 10
vetor2 = [0] * 10
vetor_resultado = [0] * 10

# Ler os valores do primeiro vetor

print("Digite os valores do primeiro vetor:")
for i in range(10):
    vetor1[i] = float(input(f'Digite o valor {i+1}: '))

# Ler os valores do segundo vetor

print("\nDigite os valores do segundo vetor:")
for i in range(10):
    vetor2[i] = float(input(f'Digite o valor {i+1}: '))

# Realizar a soma dos vetores e armazenar o resultado no vetor de resultado

for i in range(10):
    vetor_resultado[i] = vetor1[i] + vetor2[i]

# Imprimir os três vetores

print("\nVetor 1:")
for i in range(10):
    print(vetor1[i])

print("\nVetor 2:")
for i in range(10):
    print(vetor2[i])

print("\nVetor Resultado:")
for i in range(10):
    print(vetor_resultado[i])