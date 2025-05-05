ultimo = 10
fila = list(range(1, ultimo + 1))
operacao = " "
verifica = True


while verifica:

    print(f"Existem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print(f"F - Adicionar Cliente\nA - Realizar o Atendimento\nS - Sair")
    operacao = input("Informe a opção desejada: ").upper()

    for i in range(len(operacao)):
        
        comando = operacao[i]

        match(comando):

            case 'F':

                ultimo += 1
                fila.append(ultimo)
                print("Cliente adicionado!")

            case 'A':

                if len(fila) > 0:

                    atendido = fila.pop(0)
                    print(f"Cliente {atendido} atendido")
                    
                else:

                    print("Fila Vazia! Ninguém para atender!")

            case 'S':

                break

            case _:

                print("ERRO")

    resposta = input("REALIZAR NOVA SEQUÊNCIA DE COMANDOS? (S/N): ").upper()
    
    if resposta == "N":
        break
    