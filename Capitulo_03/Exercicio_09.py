#Escreva um programa que leia a quantidade de dias, horas, minutos e 
#segundos do usuário. Calcule o total em segundos. 

print("\n---------------------------------------------------------")

dia = int(input("INFORME O TOTAL DE DIAS: "))
hora = int(input("INFORME O TOTAL DE HORAS: "))
minuto = int(input("INFORME O TOTAL DE MINUTOS: "))
segundo = int(input("INFORME O TOTAL DE SEGUNDOS: "))

total_segundos = segundo + (minuto * 60) + (hora * 3600) + (dia * 86400)

print("\n---------------------------------------------------------")
print("TOTAL INFORMADO EM SEGUNDOS: ", total_segundos)