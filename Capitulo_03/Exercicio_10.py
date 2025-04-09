#Faça um programa que calcule o aumento de um salário. Ele deve 
#solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento 
#e do novo salário.

valor_salario = float(input("INFORME O VALOR DO SALÁRIO: R$"))
perc_aumento = float(input("INFORME O PERCENTUAL DE AUMENTO: "))

aumento_salario = valor_salario * perc_aumento
salario_final = valor_salario + aumento_salario

print("\n-----------------------------------------------")
print("AUMENTO DE SALÁRIO: R${:.2f}".format(aumento_salario))
print("SALÁRIO FINAL: R${:.2f}".format(salario_final))