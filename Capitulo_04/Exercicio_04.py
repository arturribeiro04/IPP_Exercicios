#Escreva um programa que pergunte o salário do funcionário e calcule 
#o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 
#10%. Para os inferiores ou iguais, de 15%. 

aumento = 0

salario_funcionario = float(input("INFORME O SALÁRIO DO FUNCIONÁRIO: R$"))

if salario_funcionario > 1250:

    aumento = salario_funcionario * 0.1

else:

    aumento = salario_funcionario * 0.15

print("-" * 120)
print("AUMENTO: R${:.2f}".format(aumento))
print("-" * 120)