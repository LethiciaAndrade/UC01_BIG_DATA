# Calcular o valor de uma prestação
prestacao = float(input("Informe o valor da prestacao:"))
tempo = int(input("Informe a quantidade de meses em atraso:"))
taxa = float(input("Informe a taxa de juros:"))   
valor_final = prestacao+(prestacao*taxa/100*tempo)                          
print(f"O valor em atraso será de R$ {valor_final:.2f}")
