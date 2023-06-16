#13- Escreva um algoritmo que:

#a- leia uma frase de 50 caracteres;

#b- conte quantos brancos existem na frase;

#c- conte quantas vezes a letra “A” aparece;

#d- imprima o que foi calculado nos itens b e c.


# Lendo a frase de 50 caracteres

frase = input("Digite uma frase de 50 caracteres: ")

# Contando os espaços em branco

contagem_brancos = 0
for caractere in frase:
    if caractere == " ":
        contagem_brancos += 1

# Contando as ocorrências da letra "A"

contagem_letra_A = 0
for caractere in frase:
    if caractere == "A" or caractere == "a":
        contagem_letra_A += 1

# Imprimindo os resultados

print("Número de espaços em branco na frase:", contagem_brancos)
print("Número de vezes que a letra 'A' aparece na frase:", contagem_letra_A)

