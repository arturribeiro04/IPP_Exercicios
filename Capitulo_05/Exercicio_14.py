numero = int(input("Informe um número inteiro: "))
cont = 0
soma = 0

while numero != 0:

    cont += 1
    soma += numero
    numero = int(input("Informe um número inteiro: "))

if cont == 0:

    print("Nenhum valor inserido!")

else: 

    media = soma / cont
    
    print("QT. de números: " + str(cont))
    print("Soma dos números: " + str(soma))
    print("Média dos números: " + str (media))