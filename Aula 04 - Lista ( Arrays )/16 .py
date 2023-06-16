#16- Dado um vetor de 128 elementos, verificar se existe um elemento igual a K (chave) no vetor. Se existir, imprimir a posição onde foi encontrada a chave; se não; imprimir a mensagem:**
#“CHAVE K NÃO ENCONTRADA”. O vetor A e a chave K são lidos a partir de uma unidade de entrada.

vetor = []

# Lendo o vetor de 128 elementos

for _ in range(128):
    elemento = int(input("Digite um elemento do vetor: "))
    vetor.append(elemento)

# Lendo a chave K

chave = int(input("Digite a chave K: "))

# Verificando se a chave K existe no vetor

encontrada = False
posicao = -1
for i in range(len(vetor)):
    if vetor[i] == chave:
        encontrada = True
        posicao = i
        break

# Imprimindo a posição ou a mensagem

if encontrada:
    print("Chave", chave, "encontrada na posição", posicao)
else:
    print("Chave", chave, "não encontrada")