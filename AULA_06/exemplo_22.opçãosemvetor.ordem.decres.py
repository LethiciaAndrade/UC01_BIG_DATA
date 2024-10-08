nomes = []
médias = []
resp = "S"
while resp == "S" or resp == "s":
    nomes.append(input("Informe o nome do Estudante: ")) #objetivo do "append" é acrescentar um elemento ao final de uma lista
    médias.append(float(input("Informe a média do estudante: ")))
    resp = input("Deseja continuar (S/N)? ")
print(f"A maior média da turma é: {max(médias)}.")
print(f"A menor média da turma é: {min(médias)}.")
print(f"A média da turma é: {sum(médias)/ len(médias)}.")
for i in range (len(médias)):
    print(i, " - ", nomes [i], " - ", médias[i])
médias.sort(reverse = "false") # "reverse = "false"", coloca em ordem decrescente
print(médias)