# Analise de Vendas em Python

# Dados das vendas
vendas = [
    {"produto": "Caderno", "preco": 20.0, "quantidade": 15},
    {"produto": "Caneta", "preco": 4.5, "quantidade": 50},
    {"produto": "Mochila", "preco": 120.0, "quantidade": 8},
    {"produto": "Garrafa", "preco": 45.0, "quantidade": 12},
    {"produto": "Livro", "preco": 35.0, "quantidade": 20}
]

# Calcula o faturamento total
faturamento_total = 0

for item in vendas:
    subtotal = item["preco"] * item["quantidade"]
    faturamento_total += subtotal

# Calcula o faturamento médio por produto 
quantidade_produtos = 5
faturamento_medio = faturamento_total / quantidade_produtos

# Produto com menor quantidade vendida 

produto_menor_quantidade_vendida = vendas[0]["produto"]

menor_quantidade = vendas[0]["quantidade"]

for item in vendas:
    if item["quantidade"] < menor_quantidade:
        menor_quantidade = item["quantidade"]
        produto_menor_quantidade_vendida = item["produto"]


# Descobre qual produto vendeu mais unidades
produto_mais_vendido = ""
maior_quantidade = 0

for item in vendas:
    if item["quantidade"] > maior_quantidade:
        maior_quantidade = item["quantidade"]
        produto_mais_vendido = item["produto"]

# Mostra os resultados na tela
print("--- RELATÓRIO DE VENDAS ---")
print(f"Faturamento Total: R$ {faturamento_total:.2f}")
print(f"Faturamento Médio: R$ {faturamento_medio:.2f}")
print(f"Produto menos vendido: {produto_menor_quantidade_vendida}")
print(f"Produto mais vendido: {produto_mais_vendido} ({maior_quantidade} unidades)")

