#Escreva um programa para calcular a redução do tempo de vida de 
#um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos 
#ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, 
#e calcule quantos dias de vida um fumante perderá. Exiba o total em dias.

print("\n--------------- CÁLCULO DE DIAS PERDIDOS ---------------------\n")

qt_ano = int(input("Há quantos anos você fuma? :"))
qt_cigarro_dia = int(input("Quantos cigarros você fuma ao longo de 1 dia? :"))

qt_total_cigarro = (qt_ano * 365) * qt_cigarro_dia
reducao_vida = qt_total_cigarro * 10
reducao_dias = reducao_vida / 1440

print("\n------------------------------------------")
print("TOTAL DE DIAS PERDIDOS: {:.1f} dia(s)".format(reducao_dias))


