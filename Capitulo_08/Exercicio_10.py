atual = 0
segundo = 0
terceiro = 0
termo = 10

for i in range(termo):

    if i == 0:
        
        print(atual)
        terceiro = 1

    else:

        atual = segundo + terceiro

        print(atual)

        terceiro = segundo
        segundo = atual