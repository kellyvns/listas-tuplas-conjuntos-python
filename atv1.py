estoque_despensa = ["arroz", "feijão", "óleo", "sal"]

while True:
  item = input("Digite o nome do produto (ou 'sair' para encerrar): ")

  item = item.strip().lower()

  if item == "sair":
    print("Encerrando o programa..")
    break

  if item in estoque_despensa:
    print("O produto está disponível no estoque!")
  else:
    print("O produto não está disponível no estoque!")