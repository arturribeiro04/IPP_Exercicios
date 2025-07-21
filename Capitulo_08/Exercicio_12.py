def valida_nome(lista,nome):

    resp = False

    for i in range(len(lista)):

        if lista[i] == nome:
            resp = True
            break

    return resp

lista_nome = ["JOÃO","MATEUS","RENATA","MURILO","ANA","SOFIA"]
nome = str(input("INFORME O NOME: ")).upper()

print(valida_nome(lista_nome,nome))