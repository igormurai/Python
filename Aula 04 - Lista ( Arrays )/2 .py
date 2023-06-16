#2- Escreva um algoritmo que leia um conjunto de 10 notas, armazene-as em uma variável composta chamada NOTA e calcule e imprima a sua média.

NOTA = []

# Lendo as 10 notas

for i in range(1, 11):
    nota = float(input("Digite a nota {}:".format(i)))
    NOTA.append(nota)

# Calculando a média

soma = sum(NOTA)
media = soma / len(NOTA)

# Imprimindo a média

print(f" A média das notas é: {media}" )