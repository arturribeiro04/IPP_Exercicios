#Escreva um programa que leia três números e que imprima o maior e o menor

mensagem = " "
numero_um = int(input("INFORME O NÚMERO 1: "))
numero_dois = int(input("INFORME O NÚMERO 2: "))
numero_tres = int(input("INFORME O NÚMERO 3: "))

if numero_um > numero_dois and numero_um > numero_tres:
    
    if numero_dois > numero_tres:

        mensagem = "MAIOR: {} - MENOR: {}".format(numero_um,numero_tres)

    else:

        mensagem = "MAIOR: {} - MENOR: {}".format(numero_um,numero_dois)

if numero_dois > numero_um and numero_dois > numero_tres:
    
    if numero_um > numero_tres:

        mensagem = "MAIOR: {} - MENOR: {}".format(numero_dois,numero_tres)

    else:

        mensagem = "MAIOR: {} - MENOR: {}".format(numero_dois,numero_um)

if numero_tres > numero_dois and numero_tres > numero_um:
    
    if numero_dois > numero_um:

        mensagem = "MAIOR: {} - MENOR: {}".format(numero_tres,numero_um)

    else:

        mensagem = "MAIOR: {} - MENOR: {}".format(numero_tres,numero_dois)

print(mensagem)