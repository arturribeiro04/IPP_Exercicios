lista_um = []
lista_dois = []
lista_tres = []

print("--- LISTA UM ---")
numero = int(input("Informe um número: "))

while numero != 0:

    lista_um.append(numero)
    numero = int(input("Informe um número: "))

print("--- LISTA DOIS ---")
numero = int(input("Informe um número: "))

while numero != 0:

    lista_dois.append(numero)
    numero = int(input("Informe um número: "))

for x in range(len(lista_um)):

    lista_tres.append(lista_um[x])

for x in range(len(lista_dois)):

    lista_tres.append(lista_dois[x])

print("-" * 20)
print(f"LISTA UM: {lista_um}")
print(f"LISTA DOIS: {lista_dois}")
print(f"LISTA TRÊS: {lista_tres}")
print("-" * 20)