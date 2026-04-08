carrinho = {"Item1": 50, "Item2": 100, "Item3": 20}

valor = carrinho.pop("Item2")
print("O item de valor", valor, "foi removido")

valor2 = carrinho.pop("Item4", None)
print("Tentativa de remover Item4:", valor2)