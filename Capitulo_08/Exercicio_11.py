def validar_tam_string(string,minimo, maximo):

    resp = True if minimo <= len(string) <= maximo else False

    return resp

variavel_string = str(input("INFORME A STRING: "))
tam_min = int(input("INFORME O TAMANHO MÍNIMO DA STRING: "))
tam_max = int(input("INFORME O TAMANHO MÁXIMO DA STRING: "))

print(validar_tam_string(variavel_string,tam_min,tam_max))