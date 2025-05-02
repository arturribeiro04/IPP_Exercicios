tabuada = int(input("Informe qual tabuada será mostrada: "))
tabuada_ini = int(input("Informe o início da tabuada: "))
tabuada_fim = int(input("Informe o final da tabuada: "))

print("-" * 10 + "Tabuada do" + str(tabuada) + "-" * 10)

for i in range(tabuada_ini,tabuada_fim + 1,1):
    print(str(tabuada) + " X " + str(i) + " = " + str(i * tabuada))