#Escreva um programa que calcule o preço a pagar pelo fornecimento 
#de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de insta
#lação: R para residências, I para indústrias e C para comércios. 
preco_unitario = 0

energia_consumida = float(input("INFORME A QT. DE KW/H CONSUMIDA: "))
print("\nR - RESIDENCIAL\nI - INDUSTRIAL\nC - COMERCIAL\n")
tipo_instalacao = input("INFORME O TIPO DE INSTALAÇÃO: ").upper()


match(tipo_instalacao):

    case 'R':

        if energia_consumida <= 500:
                  
                preco_unitario = 0.4
        else:
                  
                preco_unitario = 0.65
    case 'C':

        if energia_consumida <= 1000:
                  
                preco_unitario = 0.55
        else:
                  
                preco_unitario = 0.60
    case 'I':

        if energia_consumida <= 5000:
                  
                preco_unitario = 0.55
        else:
                  
                preco_unitario = 0.60
    case _:

        print("ERRO")

preco_final = energia_consumida * preco_unitario

print("-" * 120)
print("PREÇO FINAL: R${:.2f}".format(preco_final))
print("-" * 120)