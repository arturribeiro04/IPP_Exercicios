lista_um = [1,3,3,10,4,7,8,9,8,1,3]
lista_dois = [23,4,5,5,6,1,2,9,8,34,2,1,8]
lista_tres = []

valida = True

for i in range(len(lista_um)):

    valida = True
    comparador = lista_um[i]

    if i == 0:

        lista_tres.append(comparador)

    else:

        for j in range(len(lista_tres)):

            if comparador == lista_tres[j]:

                valida = False
                break
            else: 
                 valida = True
        
        if valida == True:

            lista_tres.append(comparador)

for i in range(len(lista_dois)):

    valida = True
    comparador = lista_dois[i]

    if i == 0:

        lista_tres.append(comparador)

    else:

        for j in range(len(lista_tres)):

            if comparador == lista_tres[j]:

                valida = False
                break
            else: 
                 valida = True
        
        if valida == True:

            lista_tres.append(comparador)

print(lista_tres)

