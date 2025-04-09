#Escreva um programa que calcule o tempo de uma viagem de carro. 
#Pergunte a distância a percorrer e a velocidade média esperada para a viagem. 
print("\n----------------------------------------------")


distancia = float(input("INFORME A DISTÂNCIA (KM): "))
velocidade_media = float(input("INFORME A VELOCIDADE MÉDIA (KM/H): "))

viagem = distancia / velocidade_media

print("\n----------------------------------------------")
print("DURAÇÃO DA VIAGEM: {:.1f} h".format(viagem))