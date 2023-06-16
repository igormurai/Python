#3- Repita o algoritmo acima, porém imprima quantos valores estão acima da média.

NOTA = []

# Lendo as 10 notas

for i in range(1, 11):
    nota = float(input("Digite a nota {}:".format(i)))
    NOTA.append(nota)

# Calculando a média

soma = sum(NOTA)
media = soma / len(NOTA)

acima_media = 0
for nota in NOTA:
    if nota > media:
        acima_media += 1

# Imprimindo a média e as notas acima da média

print(f" A média das notas é: {media}" )
print(f" Quantidade de valores acima da média: {acima_media}" )