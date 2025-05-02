pontos = 0 
questao = 1

while questao<= 3: 

    resposta= input(f"Resposta da questão {questao}: ").upper()

    if questao== 1 and resposta== "B": 

        pontos= pontos + 1 

    if questao== 2 and resposta== "A": 

        pontos= pontos + 1 

    if questao== 3 and resposta== "D": 

        pontos= pontos+ 1 

    questao = questao + 1 
    
print(f"O aluno fez {pontos} ponto(s)" ) 