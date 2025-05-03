valor = float(input(" Digite o valor a pagar:")) 

while valor != 0:

    while not(valor >= 0.01) or valor == 0:
        valor = float(input(" Digite um valor a pagar válido:")) 

    cédulas = 0 
    atual = 10000
    apagar = valor * 100

    while True: 

        if atual <= apagar: 

            apagar -= atual 
            cédulas += 1

        else: 

            print(f"{cédulas} cédula (s) de R${atual / 100}") 
            
            if apagar == 0: 

                break 

            if atual == 10000:

                atual = 5000

            elif atual == 5000 : 

                atual= 2000

            elif atual == 2000: 

                atual = 1000 

            elif atual == 1000:

                atual = 500 

            elif atual == 500: 

                atual = 200
            
            elif atual == 200:

                atual = 100
            
            elif atual == 100:

                atual = 50

            elif atual == 50:

                atual = 25

            elif atual == 25:

                atual = 10

            elif atual == 10:

                atual = 5

            elif atual == 5:

                atual = 1

            cédulas = 0

    valor = float(input(" Digite o valor a pagar:")) 

print("FIM DO PROGRAMA!")