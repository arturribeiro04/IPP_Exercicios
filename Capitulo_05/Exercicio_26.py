dividendo = int(input("Informe o dividendo: "))
divisor = int(input("Informe o divisor: "))

quociente = 0

while dividendo >= divisor:

    dividendo -= divisor
    quociente += 1

resto = dividendo

print("Quociente: " + str(quociente))
print("Resto: " + str(resto))
