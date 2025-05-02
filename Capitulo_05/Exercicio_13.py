divida_inicial = float(input("Informe o valor inicial da dívida: R$"))
juros_mensais = float(input("Informe os juros mensais: "))
valor_mensal = float(input("Informe o valor mensal a ser pago: R$"))
nr_meses = 0
total_pago = 0
total_juros = 0

divida = divida_inicial
pagamento_mensal = divida_inicial * juros_mensais

if valor_mensal < pagamento_mensal:

    print("-" * 20)
    print("AVISO!")
    print("-" * 20)

    print("Não será possível quitar com esse valor mensal, pois está abaixo do valor dos juros mensais!")
    print("Valor Mensal: R${:.2f}".format(valor_mensal))
    print("Juros Mensais: R${:.2f}".format(pagamento_mensal))

else:

    while divida > valor_mensal:

        calculo_juros = divida * juros_mensais
        abatimento = valor_mensal - (calculo_juros)
        divida = divida - abatimento
    
        total_juros = total_juros + calculo_juros
        nr_meses = nr_meses + 1
        total_pago = total_pago + valor_mensal
 
    print(divida)

    if divida != 0:

        calculo_juros = divida + (divida * juros_mensais)
        divida = calculo_juros
        valor_mensal = calculo_juros
        divida = divida - valor_mensal

        total_juros = total_juros + calculo_juros
        nr_meses = nr_meses + 1
        total_pago = total_pago + valor_mensal


    print(divida)
    print("-" * 20)

    print("Nº de meses para quitar a dívida: " + str(nr_meses))
    print("Total pago: R${:.2f}".format(total_pago))
    print("Total de juros pago: R${:.2f}".format(total_juros))