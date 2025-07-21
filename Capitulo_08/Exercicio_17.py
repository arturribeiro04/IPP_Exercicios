def gerador_primo():

    numero = 1
 
    while numero < 20:

        cont = 0

        for i in range(1,numero + 1,1):

            cont += 1 if numero % i == 0 else 0

        if cont == 2:
            
            yield numero
        
        numero += 1

for i in gerador_primo():

    print(i, end=" ")