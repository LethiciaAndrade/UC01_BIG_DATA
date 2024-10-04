# Entrada de Dados e Tratamento de Erros (comando "try"- executa a ação; "except"- vai verificar se e que tipo de erro é)
try:
    n1 = int(input("Informe o Primeiro Valor: "))
    n2 = int(input("Informe o Segundo Valor: "))
except ValueError:  #Verifica o erro caso o usuário digite uma letra, ao invés de nº inteiro
    print("Verifique a Entrada de dados")
else:
    try:
        result = n1 / n2
    except ZeroDivisionError:
        print("Não é possível dividir por zero.")
    else:
        print(result)


