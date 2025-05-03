numero = int(input("Informe um número: "))
cont = 0

for divisor in range(1 , numero + 1 , 1):

    if numero % divisor == 0:
        cont += 1

if cont == 2:
    print("NÚMERO PRIMO")
else:
    print("NÚMERO COMPOSTO")

