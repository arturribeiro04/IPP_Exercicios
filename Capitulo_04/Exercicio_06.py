#Escreva um programa que pergunte a distância que um passageiro 
#deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km 
#para viagens de até de 200 km, e R$ 0,45 para viagens mais longas. 

distancia_km = float(input("INFORME A QUILOMETRAGEM À PERCORRER: "))

if distancia_km <= 200:

    preco_passagem = distancia_km * 0.5

else:

    preco_passagem = distancia_km * 0.45

print("-" * 120)
print("PREÇO DA PASSAGEM: R${:.2f}".format(preco_passagem))
print("-" * 120)