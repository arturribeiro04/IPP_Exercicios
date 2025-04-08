resultado = ""
materia_1 = float(input("Informe a nota da matéria 1: "))
materia_2 = float(input("Informe a nota da matéria 2: "))
materia_3 = float(input("Informe a nota da matéria 3: "))

MEDIA_PADRAO = 7

if materia_1 >= 7 and materia_2 >= 7 and materia_3 >= 7:

    resultado = "APROVADO"

else:
    
    resultado = "REPROVADO"

print(resultado)