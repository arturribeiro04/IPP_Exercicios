def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

def mmc(a, b):
    return abs(a * b) // mdc(a, b)

a = 12
b = 18
resultado = mmc(a, b)
print(f"O M.M.C. de {a} e {b} é {resultado}")