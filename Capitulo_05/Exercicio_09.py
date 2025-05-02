numero_um = int(input("Informe o número 1: "))
numero_dois = int(input("Informe o número 2: "))

quociente = 0
resto = 0
dividendo = numero_um
divisor = numero_dois

while dividendo > divisor:

    dividendo = dividendo - divisor
    quociente = quociente + 1

resto = dividendo

print("Quociente: {}".format(quociente))
print("Resto: {}".format(resto))