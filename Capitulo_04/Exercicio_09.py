#Escreva um programa para aprovar o empréstimo bancário para com
#pra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e 
#a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 
#30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar 
#dividido pelo número de meses a pagar. 

mensagem = " "
valor_casa = float(input("INFORME O VALOR DA CASA: R$"))
salario = float(input("INFORME O SALÁRIO: R$"))
qt_ano = int(input("EM QUANTOS ANOS? :"))

qt_meses = qt_ano * 12
comp_salario = salario * 1.3

valor_prestacao = valor_casa / qt_meses

if valor_prestacao > comp_salario:

    mensagem = "A COMPRA NÃO PODE SER REALIZADA! VALOR EXCEDENTE À 30% DO SALÁRIO"

else:

    mensagem = "VALOR DA PRESTAÇÃO: R${:.2f}".format(valor_prestacao)

print("-" * 120)
print(mensagem)
print("-" * 120)