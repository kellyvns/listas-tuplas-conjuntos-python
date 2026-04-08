perfil_usuario = {
    "nome": "Kelly",
    "email": "kelly@email.com",
    "status": "inativo"
}

perfil_usuario["status"] = "ativo"

if "idade" not in perfil_usuario:
    perfil_usuario["idade"] = 25

for chave in perfil_usuario.keys():
    print(chave)