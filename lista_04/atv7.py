nomes_sujos = ["ana", "pedro", "ANA", "marcos", "pedro", "beatriz"]

print("Original:", nomes_sujos)

nomes_limpos = set(nome.capitalize() for nome in nomes_sujos)

print("Limpos:", list(nomes_limpos))