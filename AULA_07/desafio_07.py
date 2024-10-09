sexo = []
olhos = []
cabelos =[]
idade = []
resp = "S"
quantidade_sexo_idade = 0
quantidade_olhos_cabelos = 0
while resp == "S" or resp == "s":
    sexo.append(input("Informe o sexo M - Masculino ou F - Feminino" ))
    olhos.append(input("Informe a cor dos olhos A - Azuis, V - Verdes ou C- Castanhos "))
    cabelos.append(input("Informe a cor dos cabelos L - Louros, P - Pretos ou C - Castanhos "))
    idade.append(int(input("Informe a idade: ")))
    resp = input("Deseja Continuar (S/N)? ")
for i in range(len(sexo)):
    if (sexo[i]) == "F" or sexo[i] == "f" and (idade[i] >= 18 and idade <= 35):
        quantidade_sexo_idade += 1
if (olhos[i] == "V" or olhos [i] == "v") and (cabelos[i] == "L" or cabelos [i] == "1"):
    quantidade_olhos_cabelos += 1
print(f" A maior idade é {max(idade)} anos.")
print (f" A menor idade é {min(idade)} anos.")
print (f"A média das idades é {sum(idade)/ len(idade):.0f} anos.")
print(f" A quantidade de pessoas do sexo feminino com idades entre 18 e 35 anos é {quantidade_sexo_idade}")
print(f"A quantidade de pessoas que possuem cabelos louros e olhos verdes é {quantidade_olhos_cabelos}")

