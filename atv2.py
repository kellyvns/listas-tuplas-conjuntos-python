notas = []

for i in range(10):
    while True:
        entrada = input(f"Informe a nota do aluno {i+1}: ").strip()

        if entrada == "":
            print("Entrada vazia. Tente novamente!")
            continue
        try:
            nota = float(entrada)
            notas.append(nota)
            break
        except ValueError:
            print("Valor inválido. Digite apenas números.")

notas.sort(reverse=True)

print("\nNotas em ordem decrescente: ")
print(notas)

        