def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

a = 56
b = 32

resultado = mdc(a, b)

print(f"O M.D.C. de {a} e {b} é {resultado}")