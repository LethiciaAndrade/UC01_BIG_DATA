IRRF = 0.11
INSS = 0.08
sindicato = 0.05
salário_hora = (int(input("Informe seu salário por hora: ")))
hora_trabalhada = (int(input("Informe suas horas trabalhadas:  ")))
salário_bruto = salário_hora * hora_trabalhada
print(f"O salário bruto é R$", salário_bruto)
IRRF = salário_bruto * 0.11
print(f"O valor do desconto do IRRF é R$", IRRF)
INSS = salário_bruto * 0.08
print(f"O valor de desconto do INSS é R$", INSS)
sindicato = salário_bruto * 0.05
print(f"O valor do desconto do sindicato é R$", sindicato)
salário_líquido = salário_bruto - (IRRF + INSS + sindicato)
print(f"O salário líquido é: R$", salário_líquido)