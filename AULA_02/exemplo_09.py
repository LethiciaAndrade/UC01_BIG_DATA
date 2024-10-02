# Referente ao exemplo 04
import datetime
data_atual = datetime.date.today()
ano_atual= data_atual.year
nome = input("informe o seu nome: ")
ano_nasc = int(input("Informe o seu ano de nascimento: "))
idade = ano_atual - ano_nasc
print("Sr(a) ", nome, "a sua idade é: ",idade," anos.")