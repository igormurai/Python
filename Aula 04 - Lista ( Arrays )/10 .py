#10- Escreva um algoritmo que:

#a- leia 100 valores numéricos e os armazene numa variável composta unidimensional A;

#b-  calcule e escreva:

#c- calcule e escreva quantos termos da série acima têm o numerador menor do que o denominador.


# Lendo 100 valores numéricos

A = []
for _ in range(100):
    valor = float(input("Digite um valor numérico: "))
    A.append(valor)

# Calculando a série e contando os termos com numerador menor que o denominador

soma = 0
count = 0
for i in range(len(A)):
    soma += A[i] / (i + 1)
    if A[i] < (i + 1):
        count += 1

# Imprimindo a soma e o número de termos com numerador menor que o denominador

print("Soma da série:", soma)
print("Número de termos com numerador menor que o denominador:", count)
