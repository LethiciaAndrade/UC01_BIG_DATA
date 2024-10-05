soma = 0
#média = 0
for i in range (5):
    nome = input("Informe seu nome: ")
    idade = int(input("Informe sua idade: "))
    soma = soma + idade
média = soma/ (i + 1)
print(f"A soma é {soma}, a média é {média:.0f}")
