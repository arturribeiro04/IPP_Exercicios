L = [15,7,27,39]
cont = 0

p = int(input("Informe o valor a procurar: "))

for i in range(len(L)):

    if L[i] == p:
        break

    else:
        cont += 1

if cont == len(L):

    print(f"NADA ENCONTRADO!")

else:

    print(F"{p} ENCONTRADO NA POSIÇÃO {cont}")