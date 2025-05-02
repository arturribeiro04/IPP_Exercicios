numero = 1

final = int(input("Informe o último número a ser mostrado: "))

print("-" * 4 + "Números ímpares da sequência" + "-" * 4)

for i in range(numero,final+1,2):
    print(i,end=" ")