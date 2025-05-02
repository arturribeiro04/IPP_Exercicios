deposito_inicial = float(input("Informe o depósito inicial: R$"))
taxa_juros = float(input("Informe a taxa de juros: "))

juros_total = 0
CONST_MESES = 24

deposito = deposito_inicial

for i in range(CONST_MESES):

    calculo_juros = deposito * taxa_juros
    deposito = deposito +calculo_juros
    juros_total = juros_total + calculo_juros
    print("VALOR NO MÊS {}: R${:.2f}".format(i+1,deposito))

print("-" * 20)
print("Total de juros ganho: R${:.2f}".format(juros_total))