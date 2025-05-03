numero = int(input("Informe um número: "))

if numero <= 1:
    print("Não há nenhum número primo na sequência informada!")

else:

    for dividendo in range(1,numero + 1,1):

        cont = 0

        for divisor in range(1 , dividendo + 1 , 1):

            if dividendo % divisor == 0:
                cont += 1

        if cont == 2:
            print(dividendo)
            cont = 0


        




