usuários = ["Lethicia", "Letícia", "Deise", "Rayanne", "Isadora"]
senhas = ["246", "246@", "81012", "81012!", "141618"]
usuário = input("Informe o nome de acesso ao sistema: ")
for i in range(len(usuários)):
    if usuários[i] == usuário:
        resp = "Usuário Encontrado!"
        break # Verifica 
    else: 
        resp = "Usuário não Encontrado!"
        break
        print(resp)
senhas = input(f"Informe a senha de acesso ao sistema: ")
for i in range (senhas):
    if senhas [i] == senhas:
        resp = "Acesso Liberado!"
    else:
        resp = "Acesso Negado!"
        print(resp)

