soma = 0
maior = 0
for i in range(5):
    nome =input("Informe seu nome: ")
    idade = int(input("Informe sua idade: "))
    if idade > maior:
        maior = idade 
    soma = soma + idade
média = soma/ (i + 1)
print (f"A soma é {soma}")
print(f"A média é {média:.0f}")
print(f"A maior idade é {maior}")  