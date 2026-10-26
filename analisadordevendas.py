# Analisador de Vendas

# Dados de vendas
vendas = [
    {"produto": "Caderno", "preco": 20.0, "quantidade": 15},
    {"produto": "Caneta", "preco": 4.5, "quantidade": 50},
    {"produto": "Mochila", "preco": 120.0, "quantidade": 8},
    {"produto": "Garrafa", "preco": 45.0, "quantidade": 12},
    {"produto": "Livro", "preco": 35.0, "quantidade": 20}
]

# Calcula quanto a loja vendeu no total
faturamento_total = 0

for item in vendas:
    subtotal = item["preco"] * item["quantidade"]
    faturamento_total += subtotal

# Calcula o faturamento médio por produto ou transação
faturamento_medio = faturamento_total / len(vendas)

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
print(f"Produto mais vendido: {produto_mais_vendido} ({maior_quantidade} unidades)")
print(f"Faturamento Médio: R$ {faturamento_medio:.2f}")