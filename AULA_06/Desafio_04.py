usuários = ["Lethicia", "Letícia", "Deise", "Rayanne", "Isadora"]
senhas = ["246", "246@", "81012", "81012!", "141618"]
usuário = input("Informe o nome de acesso ao sistema: ")
for i in range(len(usuários)):
    if usuários[i] == usuário:
       senhas = input("Informe a senha de acesso ao sistema: ")
    if senhas [i] == senhas:
            resp = "Acesso Liberado!"
    else:
        resp = "Senha não Confere!"
        break
else:
        resp = "Usuário não Encontrado!"
print(resp)

