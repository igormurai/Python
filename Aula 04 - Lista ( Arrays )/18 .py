#18- Faça um algoritmo qualquer que leia uma matriz A de 15 linhas por 25 colunas e imprima o seu conteúdo.


# Definindo o tamanho da matriz

linhas = 15
colunas = 25

# Criando a matriz

matriz = []

# Lendo os valores da matriz

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Digite o valor para a posição ({i+1}, {j+1}): "))
        linha.append(valor)
    matriz.append(linha)

# Imprimindo o conteúdo da matriz

print("Conteúdo da matriz:")
for i in range(linhas):
    for j in range(colunas):
        print(matriz[i][j], end=" ")
    print()