estoque_prosutos1 = (
    "Arroz","Feijão","Macarrão","Óleo","Açúcar","Café"
)

estoque_prosutos2 = (
    "Café","Leite","Pão","Manteiga","Queijo","Óleo"
)

comum = set(estoque_prosutos1) & set(estoque_prosutos2)
print("Produtos em comum:", list(comum))