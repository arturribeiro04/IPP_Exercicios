dicionario_letra = {}
comp = ' '
valida = False

frase = input("DIGITE UMA FRASE: ")

for i in range(len(frase)):

    comp = frase[i]

    if comp == ' ':

        continue

    valida = comp in dicionario_letra

    if valida == True:

        dicionario_letra[comp] = +1
    
    else:

        dicionario_letra[comp] = 1

print(dicionario_letra)

