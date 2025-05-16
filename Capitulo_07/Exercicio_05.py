frase_um = "AATTGGAA"
frase_dois = "TG"

resultado = ''.join(caracter for caracter in frase_um if caracter not in frase_dois)

print(resultado)