leitura = "TTAAC"
lista_comparador = []
comparador = None
valida = True
cont = 0

for i in range(len(leitura)):
    
    if i == 0:
        lista_comparador.append(leitura[i])

    else:

        comparador = leitura[i]
        valida = True

        for j in range(len(lista_comparador)):

            if comparador == lista_comparador[j]:
                
                valida = False
                break
             
            else:

                valida = True
        
        if valida == True:

            lista_comparador.append(comparador)

for i in range(len(lista_comparador)):

    cont = 0

    for j in range(len(leitura)):

        if lista_comparador[i] == leitura[j]:

            cont += 1

    print(f"{lista_comparador[i]} : {cont}")


