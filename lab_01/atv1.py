vendas = {
    'Produto A': 300,
    'Produto B': 80,
    'Produto C': 60,
    'Produto D': 200,
    'Produto E': 250,
    'Produto F': 30
}

total = sum(vendas.values())
mais_vendido = max(vendas, key=vendas.get)

print("Total de vendas:", total)
print("Produto mais vendido:", mais_vendido)