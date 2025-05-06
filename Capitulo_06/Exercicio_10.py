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

        print(f"P FOI ENCONTRADO PRIMEIRO NA POSIÇÃO {posicao_p}")
        print(f"V FOI ENCONTRADO NA POSIÇÃO {posicao_v}")

    elif posicao_v < posicao_p:

        print(f"V FOI ENCONTRADO PRIMEIRO NA POSIÇÃO {posicao_v}")
        print(f"P FOI ENCONTRADO NA POSIÇÃO {posicao_p}")

elif achou_p == True and achou_v == False:

    print(f"SOMENTE P FOI ENCONTRADO NA POSIÇÃO {posicao_p}")

elif achou_p == False and achou_v == True:

    print(f"SOMENTE V FOI ENCONTRADO NA POSIÇÃO {posicao_v}")