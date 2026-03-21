mesas = [None] * 15

while True:
    print("\n1- Reservar\n2- Cancelar\n3- Status\n4- Sair")
    op = input("Escolha: ")

    if op == "1":
        pos = int(input("Mesa (0 a 14): "))
        if 0 <= pos < 15:
            if mesas[pos] is None:
                nome = input("Nome: ")
                mesas[pos] = nome
            else:
                print("Mesa já ocupada!")
    
    elif op == "2":
        pos = int(input("Mesa (0 a 14): "))
        if 0 <= pos < 15:
            mesas[pos] = None
    
    elif op == "3":
        livres = mesas.count(None)
        ocupadas = 15 - livres
        print("Livres:", livres, "| Ocupadas:", ocupadas)
    
    elif op == "4":
        break