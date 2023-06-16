#nsal que indica para cada mercadoria o preço de venda. Escreva o algoritmo para calcular o faturamento mensal do armazém.


# Tabela de preços de venda das mercadorias

tabela_precos = [
    10.99,  # Mercadoria 0
    5.99,   # Mercadoria 1
    15.99,  # Mercadoria 2
    # Adicione os preços para as demais mercadorias aqui...
]

# Quantidades vendidas de cada mercadoria

quantidades_vendidas = [
    15,  # Quantidade vendida da mercadoria 0
    20,  # Quantidade vendida da mercadoria 1
    10,  # Quantidade vendida da mercadoria 2
    # Adicione as quantidades vendidas para as demais mercadorias aqui...
]

# Cálculo do faturamento mensal

faturamento_mensal = 0.0
for i in range(len(quantidades_vendidas)):
    preco = tabela_precos[i]
    quantidade = quantidades_vendidas[i]
    faturamento_mensal += preco * quantidade

# Imprimindo o faturamento mensal

print("O faturamento mensal do armazém é de R$", faturamento_mensal)

