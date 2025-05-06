sequencia_parenteses = input("Informe a sequência de parênteses: ")
pilha_parenteses = []
cont = 0

for i in range(len(sequencia_parenteses)):
    
    if i == 0 and sequencia_parenteses[0] == ')':
        print("ERRO")
        break

    else:

        if len(pilha_parenteses) == 0 and sequencia_parenteses[i] == ')':
            cont -= 1
            break
        
        if sequencia_parenteses[i] == ')':
            
            if pilha_parenteses[0] == '(':

                pilha_parenteses.pop(0)
                cont -= 1

        elif sequencia_parenteses[i] == '(':

            pilha_parenteses.append('(')
            cont += 1
    
    print(cont)
                

if len(pilha_parenteses) == 0 and cont == 0:

    print("OK: " + sequencia_parenteses)

else:
    print("ERRO")
