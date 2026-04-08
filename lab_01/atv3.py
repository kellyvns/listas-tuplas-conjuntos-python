estoque = {}

estoque["Teclado"] = 150.00
estoque["Mouse"] = 80.00
estoque["Monitor"] = 900.00

for produto, preco in estoque.items():
    print(f"Produto: {produto} - R$ {preco}")