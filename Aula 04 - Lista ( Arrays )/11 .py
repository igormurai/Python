#11- Faça um algoritmo que leia um conjunto de 10 elementos reais e os coloque em um vetor.
#Construa um segundo vetor formado da seguinte maneira:

#• Os elementos de ordem par são os correspondentes do primeiro vetor multiplicados por 3.
#• Os elementos de ordem ímpar são os correspondentes do primeiro vetor divididos por 2.
#• Imprima os dois vetores.


# Definindo o primeiro vetor

primeiro_vetor = []

# Lendo os valores e armazenando no primeiro vetor

for i in range(10):
    valor = float(input("Digite um valor real: "))
    primeiro_vetor.append(valor)

# Construindo o segundo vetor

segundo_vetor = []
for i in range(10):
    if i % 2 == 0:

        # Elementos de ordem par: multiplicar por 3

        segundo_vetor.append(primeiro_vetor[i] * 3)
    else:
        # Elementos de ordem ímpar: dividir por 2

        segundo_vetor.append(primeiro_vetor[i] / 2)

# Imprimindo os vetores

print("Primeiro vetor:", primeiro_vetor)
print("Segundo vetor:", segundo_vetor)
