fator_um = int(input("Informe o fator 1: "))
fator_dois = int(input("Informe o fator 2: "))

print(str(fator_um) + " X " + str(fator_dois) + " = ",end="")


for i in range(fator_dois):

    print(fator_um, end="")
    
    if i != fator_dois - 1:
        
        print(" + ", end="")

print(" = ", end="")

for i in range(fator_um):
    
    print(fator_dois, end="")
    
    if i != fator_um - 1:
    
        print(" + ", end="")