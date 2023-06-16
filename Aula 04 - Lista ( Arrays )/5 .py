#5- Ler um vetor de 10 elementos numéricos e verificar se existem elementos iguais a 30. Se existirem, escrever as posições em que estão armazenados.

vetor = []

# Lendo os elementos do vetor

for i in range(10):
    elemento = int(input("Digite o elemento {}: ".format(i + 1)))
    vetor.append(elemento)

# Verificando se existem elementos iguais a 30

posicoes = []
for i in range(len(vetor)):
    if vetor[i] == 30:
        posicoes.append(i)

# Imprimindo as posições dos elementos iguais a 30

if len(posicoes) > 0:
    print("Elemento igual a 30 encontrado nas posições:", posicoes)
else:
    print("Não existem elementos iguais a 30 no vetor.")