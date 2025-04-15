#Escreva um programa que pergunte a velocidade do carro de um 
#usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário 
#foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 
#80 km/h.

LIMITE = 80
VALOR = 5
velocidade_carro = float(input("INFORME A VELOCIDADE DO CARRO: "))

if velocidade_carro > LIMITE:
    valor_multa = (velocidade_carro - LIMITE) * VALOR
    mensagem = "MULTA NO VALOR DE R${:.2f}".format(valor_multa)

else:
    mensagem = "DENTRO DO LIMITE DE VELOCIDADE"

print("-" * 120)
print(mensagem)
print("-" * 120)