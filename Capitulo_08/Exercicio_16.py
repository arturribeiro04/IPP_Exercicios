def imprimir_lista(lista, nivel=0):

    for elemento in lista:

        if type(elemento) == list:

            imprimir_lista(elemento, nivel + 1)
        else:

            print('   ' * nivel + str(elemento))

L = [1, [2, 3, 4, [5, 6, 7]]]

imprimir_lista(L)