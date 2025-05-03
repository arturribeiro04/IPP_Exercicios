def raiz_quadrada_newton(n):

    b = 2
    p = (b + (n / b)) / 2

    while abs(n - p**2) >= 0.0001:
        b = p
        p = (b + (n / b)) / 2

    return p

numero = float(input("Digite um número para calcular a raiz quadrada: "))
resultado = raiz_quadrada_newton(numero)
print(f"A raiz quadrada aproximada de {numero} é {resultado:.5f}")