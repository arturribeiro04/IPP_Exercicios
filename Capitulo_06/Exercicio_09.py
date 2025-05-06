L = [15,7,27,39]
cont = 0
achou_p = False
achou_v = False
primeiro = ' '

p = int(input("Informe o valor P a procurar: "))
v = int(input("Informe o valor V a procuar: "))

for i in range(len(L)):

    if L[i] == p:

        achou_p = True
        posicao_p = i
        break
    
for i in range(len(L)):

    if L[i] == v:

        achou_v = True
        posicao_v = i
        break

if achou_p == True and achou_v == True:

    if posicao_p < posicao_v:

        print("P FOI ENCONTRADO PRIMEIRO!")

    elif posicao_v < posicao_p:

        print("V FOI ENCONTRADO PRIMEIRO!")

elif achou_p == True and achou_v == False:

    print("SOMENTE P FOI ENCONTRADO")

elif achou_p == False and achou_v == True:

    print("SOMENTE V FOI ENCONTRADO")