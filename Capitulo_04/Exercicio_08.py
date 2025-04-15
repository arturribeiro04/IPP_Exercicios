#Escreva um programa que leia dois números e que pergunte qual 
#operação você deseja realizar. Você deve poder calcular soma (+), subtração (-), 
#multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada. 

resultado = 0
mensagem = " "
termo_um = int(input("INFORME O PRIMEIRO TERMO: "))
termo_dois = int(input("INFORME O SEGUNDO TERMO: "))

print("\n1 - SOMA\n2 - SUBTRACAO\n3 - MULTIPLICAÇÃO\n4 - DIVISÃO")
opcao = int(input("ESCOLHA A OPÇÃO: "))

match(opcao):

    case 1:

        resultado = termo_um + termo_dois
        mensagem = "SOMA: {} + {} = {}".format(termo_um,termo_dois,resultado)
    
    case 2:

        resultado = termo_um - termo_dois
        mensagem = "SUBTRAÇÃO: {} - {} = {}".format(termo_um,termo_dois,resultado)

    case 3:

        resultado = termo_um * termo_dois
        mensagem = "MULTIPLICAÇÃO: {} * {} = {}".format(termo_um,termo_dois,resultado)

    case 4:

        resultado = termo_um / termo_dois
        mensagem = "DIVISÃO: {} / {} = {}".format(termo_um,termo_dois,resultado)

    case _:
        print("ERRO")

print("-" * 120)
print(mensagem)
print("-" * 120)