numero = int(input("Informe um número: "))

valida = True
comparacao = str(numero)
inverso = str(numero)
cont = len(comparacao)

for i in range(len(comparacao)):
    
    if comparacao[i] != inverso[cont-1]:

        valida = False
        break
    
    cont -= 1

if valida == True:
    print("NÚMERO PALÍNDROMO")

else:
    print("NÚMERO NÃO PALÍNDROMO")
