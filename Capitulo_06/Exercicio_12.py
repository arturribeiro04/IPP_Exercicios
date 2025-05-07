L = [1,7,2,4]
menor = 0


for i in range(len(L)):

    if i == 0:
        menor = L[i]
    
    else:

        if menor > L[i]:

            menor = L[i]

print("-" * 20)
print(f"MENOR TEMPERATURA: {menor}º")
