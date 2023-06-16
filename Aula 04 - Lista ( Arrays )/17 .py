#17- Refaça o algoritmo acima otimizando-o usando uma técnica conhecida por Pesquisa Binária. Suponha primeiramente que o vetor já esteja ordenado. Procuramos então o elemento K dividindo o vetor em duas partes e testando em qual das duas partes ele deveria estar. Procede-se então, da mesma forma para a parte provável, e assim sucessivamente. Obs.: na pesquisa sequencial simple(problema 16), o número médio de comparações que devem ser feitas até encontrar a chave é N/2, onde N é o número de elementos do vetor. Nonosso caso, no algoritmo 16, teríamos, em média, 128/2 = 64 comparações. Na pesquisa binária, o número máximo de comparações é log2N. Teríamos, então, log2128=7 comparações, no máximo.


# Lendo o vetor de 128 elementos

vetor = []
for _ in range(128):
    elemento = int(input("Digite um elemento do vetor: "))
    vetor.append(elemento)

# Ordenando o vetor

vetor.sort()

# Lendo a chave K

chave = int(input("Digite a chave K: "))

# Pesquisa binária

encontrada = False
inicio = 0
fim = len(vetor) - 1
posicao = -1

while inicio <= fim:
    meio = (inicio + fim) // 2
    if vetor[meio] == chave:
        encontrada = True
        posicao = meio
        break
    elif vetor[meio] < chave:
        inicio = meio + 1
    else:
        fim = meio - 1

# Imprimindo a posição ou a mensagem

    print("Chave", chave, "encontrada na posição", posicao)
else:
    print("Chave", chave, "não encontrada")