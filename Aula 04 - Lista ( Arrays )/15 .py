#15- Classificar um vetor numérico VET de 20 elementos em ordem crescente.


# Definindo o vetor numérico

VET = [8, 2, 15, 1, 6, 10, 5, 12, 3, 17, 4, 9, 11, 7, 19, 13, 16, 18, 14, 20]

# Tamanho do vetor

n = len(VET)

# Implementação do Selection Sort

for i in range(n-1):

    # Encontrando o índice do menor elemento não classificado

    indice_min = i
    for j in range(i+1, n):
        if VET[j] < VET[indice_min]:
            indice_min = j
    
    # Trocando os elementos de posição

    VET[i], VET[indice_min] = VET[indice_min], VET[i]

# Imprimindo o vetor classificado

print("Vetor classificado em ordem crescente:", VET)

