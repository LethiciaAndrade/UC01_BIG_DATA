nomes = []
médias = []
resp = "S"
while resp == "S" or resp == "s":
    nomes.append(input("Informe o nome do Estudante: ")) #objetivo do "append" é acrescentar um elemento ao final de uma lista
    médias.append(float(input("Informe a média do estudante: ")))
    resp = input("Deseja continuar (S/N)? ")
    print(nomes)
    print(médias)
