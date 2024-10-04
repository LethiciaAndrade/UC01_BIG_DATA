import datetime
try:
    idade = int(input("Informe sua idade: "))
    tempo = int(input("Informe o tempo trabalhado: "))
except ValueError:
    print("Verifique os dados informados")
else:
    if idade >=65:
        print("Está APTO à aposentadoria")
    elif tempo >=30: 
        print("Você está APTO à aposentadoria")
    elif idade >= 60 and tempo >= 25:
        print("Você está APTO à aposentadoria")
    else:
        print("Você está INAPTO à aposentadoria")

