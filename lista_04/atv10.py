convidados = set()

while True:
    nome = input("Nome (ou sair): ").strip()
    
    if nome.lower() == "sair":
        break
    
    if not nome.isalpha():
        print("Nome inválido!")
        continue
    
    convidados.add(nome.capitalize())

print("Lista final:", list(convidados))