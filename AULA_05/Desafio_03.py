soma_m = 0
soma_f = 0
maior = 0
cont_m = 0
cont_f = 0
maior = 0
for i in range (5):
    nome = input("Informe seu nome: ")
    sexo = input("Informe seu sexo: ")
    idade = int(input("Informe sua idade: "))    
    if idade > maior:
        maior = idade
    if sexo == "M" or sexo == "m":
        soma_m = soma_m + idade
        cont_m += 1
    if sexo == "F" or sexo == "f":
        soma_f = soma_f + idade
        cont_f += 1
media_m = soma_m / cont_m  
media_f = soma_f / cont_f      
print(f"A soma das Idades dos Homens é {soma_m}")
print(f"A soma das Idades das Mulheres é {soma_f}")
print(f"A média das Idades dos Homens é {media_m:.0f}")
print(f"A soma das Idades das Mulheres é {media_f:.0f}")
print(f"A maior idade é {maior}")

