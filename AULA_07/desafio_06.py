# O Departamento Estadual de Metereologia solicitou desenvolvimento de um programa que armazene
# em um vetor um conj. indeterminado de temperaturas, ao final, informe a menor, a maior e a média das temperaturas.
temperaturas = []
resp = "S"
while resp == "S" or resp == "s":
    temperaturas.append(float(input("Informe a temperatura: ")))
    resp = input("Deseja continuar (S/N)? ")
print(f"A maior temperatura foi: {max(temperaturas)}ºC.")
print(f"A menor temperatura foi: {min(temperaturas)}.ºC.")
print(f"A temperatura média resgistrada foi {(sum(temperaturas)/ len(temperaturas)):.1f} ºC")