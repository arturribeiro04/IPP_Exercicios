total_compra = 0

print("\n(1,2,3,5,9,0)\n")
codigo_produto = int(input("Informe o código do produto: "))
while codigo_produto != 0 and codigo_produto != 1 and codigo_produto != 2 and codigo_produto != 3 and codigo_produto != 5 and codigo_produto != 9:
    codigo_produto = int(input("Informe um código de produto válido: "))

while codigo_produto != 0:

    qt_comprada = int(input("Informe a quantidade comprada: "))

    preco_produto = 0

    match(codigo_produto):

        case 1:
            preco_produto = 0.5
        case 2:
            preco_produto = 1
        case 3:
            preco_produto = 4
        case 4:
            preco_produto = 7
        case 9:
            preco_produto = 8
        case _:
            print("ERRO")

    valor_compra = qt_comprada * preco_produto
    total_compra += valor_compra

    print("\n(1,2,3,5,9,0)\n")
    codigo_produto = int(input("Informe o código do produto: "))
    while codigo_produto != 0 and codigo_produto != 1 and codigo_produto != 2 and codigo_produto != 3 and codigo_produto != 5 and codigo_produto != 9:
        codigo_produto = int(input("Informe um código de produto válido: "))

print("-" * 20)
print("TOTAL DA COMPRA: R${:.2f}".format(total_compra))