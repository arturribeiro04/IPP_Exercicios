primeira = str(input("Informe a primeira string: ").upper())
segunda = str(input("Informe a segunda string: ").upper())
terceira = None

conjunto_um = set(primeira)
conjunto_dois = set(segunda)

conjunto_tres = conjunto_um & conjunto_dois

terceira = "".join(conjunto_tres)

print(terceira)





