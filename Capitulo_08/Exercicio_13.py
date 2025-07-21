def valida_opcao(opcao):

    while opcao != 'a' and opcao != 'b' and opcao != 'c' and opcao != 'd' and opcao != 'e':
        opcao = str(input("INFORME UMA OPÇÃO VÁLIDA (A-B-C-D-E): ")).lower()
    
    return opcao

print("OPÇÕES:\nA - B - C - D - E")
opcao = str(input("\nINFORME A OPÇÃO DESEJADA: ")).lower()
opcao = valida_opcao(opcao)