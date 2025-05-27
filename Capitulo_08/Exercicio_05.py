def pesquise(lista, valor):
    for x, e in enumerate(lista):
        if e.find(valor) != -1:
            return x
    return None

L = ['casa', 'carro', 'avião']
print(pesquise(L, 'rr'))
print(pesquise(L, 'z'))
