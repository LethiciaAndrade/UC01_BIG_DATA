import datetime
data_atual = datetime.date.today ()
try:
    nome = input("Informe seu nome: ")
    nascimento = int(input("Informe o ano de nascimento: ")) 
    ano = int(input("Informe o ano que entrou na empresa: "))
except ValueError:
    print("Verifique os dados informados")
else:
    idade = data_atual.year - nascimento
    tempo = data_atual.year - ano
    if idade >=65:
        print(f"{nome},Você está APTO à aposentadoria")
    elif tempo >=30: 
        print(f"{nome},Você está APTO à aposentadoria")
    elif idade >= 60 and tempo >= 25:
        print(f"{nome},Você está APTO à aposentadoria")
    else:
        print(f"{nome},Você está INAPTO à aposentadoria")
