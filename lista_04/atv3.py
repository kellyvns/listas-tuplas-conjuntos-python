voluntarios = []

while True:
    nome = input("Digite o nome (ou 'sair'): ").strip()
    
    if nome.lower() == "sair":
        break

    if not nome.isalpha():
        print("Nome inválido!")
        continue

    voluntarios.append(nome)

if voluntarios:
    voluntarios.sort()
    print("Voluntários:", voluntarios)
else:
    print("Lista vazia!")
    
    