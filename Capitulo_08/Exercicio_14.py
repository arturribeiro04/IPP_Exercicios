def adivinhar_numero(tentativa,numero_aleatorio):

    x = int(input("Escolha um número entre 1 e 10 :")) 

    if x == numero_aleatorio:

        print("Você acertou!")
        return 0
         
    else: 

        print(f"Você errou! Restam {tentativa - 1} erros!")
        return tentativa - 1

import random
tentativa = 3

n = random.randint(1 , 10) 

while tentativa != 0:

    tentativa = adivinhar_numero(tentativa,n)

    