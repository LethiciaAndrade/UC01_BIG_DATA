try:
    produto = input("Informe o nome do produto: ")
    quantidade = int(input("Informe a quantidade desejada: "))
    valor = float(input("Informe o valor unitário: "))
except ValueError:
    print("Verifique os valores informados")
else:
    total = quantidade * valor
    if quantidade <= 5:
        print("Desconto de 2%: ")
        desconto = total * 0.98
    elif quantidade >5 and "< = 10":
        print("Desconto de 3%")
        desconto = total * 0.97
    else:
        print(">10, Desconto de 5%")
        desconto = total * 0.95
    print(f"O valor total com desconto é R$ {desconto:.2f}")



