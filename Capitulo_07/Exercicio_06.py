frase_um = "AATTCGAA"
frase_dois = "TG"
frase_tres = "AC"

for i in range(len(frase_dois)):

    frase_um = frase_um.replace(frase_dois[i], frase_tres[i])

print(frase_um)