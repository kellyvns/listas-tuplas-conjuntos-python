notas_alunos = {
    "Ana": 8.5,
    "Bruno": 7.0,
    "Carla": 9.0
}

notas_alunos["Diego"] = 6.5

media = sum(notas_alunos.values()) / len(notas_alunos)

print("Média:", round(media, 2))