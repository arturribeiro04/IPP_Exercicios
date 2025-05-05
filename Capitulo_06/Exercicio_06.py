ultimo = 10
fila_um = list(range(1, ultimo + 1))
fila_dois = list(range(1, ultimo + 1))
operacao = " "
verifica = True


while verifica:

    print(f"Existem {len(fila_um)} clientes na fila 1")
    print(f"Fila 1 atual: {fila_um}")
    print(f"Existem {len(fila_dois)} clientes na fila 2")
    print(f"Fila 2 atual: {fila_dois}")
    print(f"F - Adicionar Cliente\nA - Realizar o Atendimento\nS - Sair")
    operacao = input("Informe a opção desejada: ").upper()

    for i in range(len(operacao)):
        
        comando = operacao[i]

        match(comando):

            case 'F':

                ultimo += 1
                fila_um.append(ultimo)
                print("Cliente adicionado à fila 1!")

            case 'G':

                ultimo += 1
                fila_dois.append(ultimo)
                print("Cliente adicionado à fila 2!")

            case 'A':

                if len(fila_um) > 0:

                    atendido = fila_um.pop(0)
                    print(f"Cliente {atendido} atendido")
                    
                else:

                    print("Fila Vazia! Ninguém para atender na fila 1!")

            case 'B':

                if len(fila_dois) > 0:

                    atendido = fila_dois.pop(0)
                    print(f"Cliente {atendido} atendido")
                    
                else:

                    print("Fila Vazia! Ninguém para atender na fila 2!")

            case 'S':

                break

            case _:

                print("ERRO")

    resposta = input("REALIZAR NOVA SEQUÊNCIA DE COMANDOS? (S/N): ").upper()
    
    if resposta == "N":
        break
    