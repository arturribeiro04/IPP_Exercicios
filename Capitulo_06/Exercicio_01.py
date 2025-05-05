lista_notas = [0,0,0,0,0,0,0]
soma = 0
x = 0

while x < 5:
    
    lista_notas[x] = float(input(f"Informe a nota {x + 1}: "))
    soma += lista_notas[x]
    x += 1

x = 0

while x < 5:
    print(f"NOTA {x + 1}: {lista_notas[x]:.1f}", end=" - ")
    x += 1

print(f"\nMédia: {soma / x:.1f}")