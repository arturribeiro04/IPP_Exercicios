# Duas listas de exemplo
lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [4, 5, 6, 7, 8, 9]

conjunto1 = set(lista1)
conjunto2 = set(lista2)

comuns = conjunto1 & conjunto2
print("Valores comuns às duas listas:", list(comuns))

so_na_primeira = conjunto1 - conjunto2
print("Valores que só existem na primeira lista:", list(so_na_primeira))

so_na_segunda = conjunto2 - conjunto1
print("Valores que só existem na segunda lista:", list(so_na_segunda))

nao_repetidos = conjunto1 ^ conjunto2
print("Elementos não repetidos nas duas listas:", list(nao_repetidos))

lista1_sem_repetidos = list(conjunto1 - conjunto2)
print("Primeira lista sem os elementos repetidos na segunda:", lista1_sem_repetidos)
