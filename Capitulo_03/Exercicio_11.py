#Faça um programa que solicite o preço de uma mercadoria e o per
#centual de desconto. Exiba o valor do desconto e o preço a pagar. 

print("\n---------------------------------------------")

preco_mercadoria = float(input("INFORME O VALOR DA MERCADORIA: R$"))
percentual_desconto = float(input("INFORME O PERCENTUAL DE DESCONTO: "))

valor_desconto = preco_mercadoria * percentual_desconto
preco_final = preco_mercadoria - valor_desconto

print("\n---------------------------------------------")
print("VALOR DE DESCONTO: R${:.2f}".format(valor_desconto))
print("PREÇO FINAL: R${:.2f}".format(preco_final))