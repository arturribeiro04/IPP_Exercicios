print("-" * 10 + " JOGO DA VELHA " + "-" * 10)

tabuleiro = [1,2,3,4,5,6,7,8,9]
jogo = False
jogador = 1
jogada = None
cont = 0
casa = None

while jogo == False:

    print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
    print("--+---+---")
    print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
    print("--+---+---")
    print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")

    jogador = 1 if cont % 2 == 0 else 2
    casa = "X" if cont % 2 == 0 else "O"


    jogada = int(input(f"\nJogador {jogador} - Informe a Jogada: "))
    jogada -= 1
    while tabuleiro[jogada] == "X" or tabuleiro[jogada] == "O":
        jogada = int(input(f"\nCasa ocupada - Informe uma outra Jogada: "))
        jogada -= 1

    match jogada:

        case 0:
            tabuleiro[jogada] = casa
        case 1:
            tabuleiro[jogada] = casa
        case 2:
            tabuleiro[jogada] = casa
        case 3:
            tabuleiro[jogada] = casa
        case 4:
            tabuleiro[jogada] = casa
        case 5:
            tabuleiro[jogada] = casa
        case 6:
            tabuleiro[jogada] = casa
        case 7:
            tabuleiro[jogada] = casa
        case 8:
            tabuleiro[jogada] = casa

    cont += 1

    if tabuleiro[0] == casa and tabuleiro[1] == casa and tabuleiro[2] == casa:
        jogo = True
        
    elif tabuleiro[3] == casa and tabuleiro[4] == casa and tabuleiro[5] == casa:
        jogo = True
        
    elif tabuleiro[6] == casa and tabuleiro[7] == casa and tabuleiro[8] == casa:
        jogo = True
        
    elif tabuleiro[0] == casa and tabuleiro[3] == casa and tabuleiro[6] == casa:
        jogo = True
        
    elif tabuleiro[1] == casa and tabuleiro[4] == casa and tabuleiro[7] == casa:
        jogo = True
        
    elif tabuleiro[2] == casa and tabuleiro[5] == casa and tabuleiro[8] == casa:
        jogo = True
        
    elif tabuleiro[2] == casa and tabuleiro[4] == casa and tabuleiro[6] == casa:
        jogo = True
        
    elif tabuleiro[0] == casa and tabuleiro[4] == casa and tabuleiro[8] == casa:
        jogo = True
        

print("RESULTADO:")

print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
print("--+---+---")
print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
print("--+---+---")
print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")

if jogo == False and cont == 9:

    print("\nVELHA")

else:

    if casa == "X":

        print("VENCEDOR: JOGADOR 1 ! - X - !")
    
    else: 

        print("VENCEDOR: JOGADOR 2 ! - O - !")