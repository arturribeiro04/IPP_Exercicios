estoque = {"TOMATE" : [1000, 2.30],
           "ALFACE" : [500, 0.45],
           "BATATA" : [2001, 1.20],
           "FEIJAO" : [100, 1.50]}

operacao = []
venda = []
resp = 'S'
valida = True

while resp != 'N':

    operacao = []

    produto = input("INFORME O NOME DO PRODUTO: ")
    valida = produto in estoque
    while valida == False:
        produto = input("INFORME UM PRODUTO NO ESTOQUE: ")
        valida = produto in estoque
    operacao.append(produto)

    quantidade = int(input("INFORME A QUANTIDADE VENDIDA: "))
    operacao.append(quantidade)

    venda.append(operacao)

    resp = input("DESEJA ADICIONAR MAIS OPERAÇÕES? : ")

#venda = [["TOMATE",5],["BATATA",10],["ALFACE",5]]
total = 0
print("VENDAS:\n")

for operacao in venda: 
    
    produto, quantidade = operacao 
    preco = estoque[produto][1] 
    custo = preco * quantidade 
    print(f"{produto:12s}: {quantidade:3d} x {preco:6.2f} = {custo:6.2f}") 
    estoque[produto][0] -= quantidade 
    total+= custo

print(f" Custo total: {total:21.2f}\n") 
print("Estoque:\n") 

for chave, dados in estoque.items():
    print("Descrição: ", chave) 
    print("Quantidade: ", dados[0]) 
    print(f"Preço: {dados[1]:6.2f}\n") 