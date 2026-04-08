votos = {
    "Design 1": 1334,
    "Design 2": 982,
    "Design 3": 1751,
    "Design 4": 210
}

total = sum(votos.values())
vencedor = max(votos, key=votos.get)
porcentagem = (votos[vencedor] / total) * 100

print("Vencedor:", vencedor)
print("Porcentagem:", round(porcentagem, 2), "%")