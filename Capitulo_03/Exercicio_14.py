#Escreva um programa que pergunte a quantidade de km percorridos 
#por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais 
#o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por 
#dia e R$ 0,15 por km rodado. 

km_percorrido = float(input("Informe a qt. de KM percorrido: "))
qt_dias = int(input("Informe a quantidade de dias de aluguel: "))

DIARIA = 60
QUILOMETRAGEM = 0.15

preco_final = (DIARIA * qt_dias) + (QUILOMETRAGEM * km_percorrido)

print("\n-------------------------------------------------------")
print("VALOR A SER PAGO: R${:.2f}".format(preco_final))