# Programa Média
nome = input("Informe o nome do estudante: ")
n1 = float(input("Informe a primeira nota de 0 a 100: "))
n2 = float(input("Informe a segunda nota de 0 a 100: "))
media = (n1 + n2) / 2
print(media)
if media >=70:
   media = (n1 + n2) / 2 
   print(f"{nome}, Congratulations, você foi Aprovado, pois sua média foi {media:.2f}")
elif media >= 30 and media <70:
   print(f"{nome}, Você está de Recuperação pois sua média foi {media:.2f}")
else:
   print(f"{nome}, Sorry, você foi Reprovado, pois sua média foi {media:.2f}")