#Escreva um programa que converta uma temperatura digitada em 
#ºC em ºF.
print("\n--------------------------------------------------------------")

temp_celsius = float(input("Informe a temperatura em °C: "))

temp_fahrenheit = ((9 * temp_celsius) / 5) + 32

print("\n--------------------------------------------------------------")
print("TEMPERATURA: {:.1f} °F".format(temp_fahrenheit))
