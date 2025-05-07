T = [-10,-8,0,1,2,4,5,-2,-4]

menor_temperatura = 0
maior_temperatura = 0
soma_temperatura = 0

for i in range(len(T)):

    if i == 0:

        menor_temperatura = T[i]
        maior_temperatura = T[i]
    
    else:

        if maior_temperatura < T[i]:

            maior_temperatura = T[i]
        
        elif menor_temperatura > T[i]:

            menor_temperatura = T[i]

    soma_temperatura += T[i]

print("-" * 20)
print(f"MAIOR TEMPERATURA: {maior_temperatura}")
print(f"MENOR TEMPERATURA: {menor_temperatura}")
print(f"MÉDIA DAS TEMPERATURAS: {soma_temperatura / i:.1f}")