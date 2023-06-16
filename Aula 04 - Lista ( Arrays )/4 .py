#4- Faça um algoritmo que leia um vetor que contém as notas de 10 alunos. Imprima o maior valor, o menor valor, a média da turma e a quantidade de notas abaixo da média.

notas = []

# Lendo as notas dos 10 alunos

for i in range(1, 11):
    nota = float(input("Digite a nota do aluno {}: ".format(i)))
    notas.append(nota)

# Calculando o maior valor

maior = max(notas)

# Calculando o menor valor

menor = min(notas)

# Calculando a média da turma

soma = sum(notas)
media = soma / len(notas)

# Contando quantas notas estão abaixo da média

abaixo_media = 0
for nota in notas:
    if nota < media:
        abaixo_media += 1

# Imprimindo os resultados

print(f"Maior valor: {maior} ")
print(f"Menor valor: {menor} ")
print(f"Média da turma: {media} ")
print(f"Quantidade de notas abaixo da média: {abaixo_media} ")