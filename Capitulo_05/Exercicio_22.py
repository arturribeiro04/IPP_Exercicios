tabuada = 1
numero = 1

print("1 - ADIÇÃO\n2 - SUBTRAÇÃO\n3 - MULTIPLICAÇÃO\n4 - DIVISÃO\n0 - SAIR\n")
opcao = int(input("Informe a opção desejada: "))

while opcao != 0:

    match(opcao):

        case 1:

            for i in range(numero,11,1):

                print("{} + {} = {}".format(tabuada, i ,tabuada + i) )

        case 2:

            for i in range(numero,11,1):

                print("{} - {} = {}".format(tabuada, i ,tabuada - i) )

        case 3:

            for i in range(numero,11,1):

                print("{} x {} = {}".format(tabuada, i ,tabuada * i) )

        case 4:

            for i in range(numero,11,1):

                print("{} / {} = {}".format(tabuada, i ,tabuada / i) )
    
    print("1 - ADIÇÃO\n2 - SUBTRAÇÃO\n3 - MULTIPLICAÇÃO\n4 - DIVISÃO\n0 - SAIR\n")
    opcao = int(input("Informe a opção desejada: "))