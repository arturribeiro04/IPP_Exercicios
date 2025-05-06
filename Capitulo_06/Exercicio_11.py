# PrograMa 6.6 - Adição de eleMentos à lista 
L = [] 

while True: 

    n = int(input( "Digite um número (0 sai):")) 
    
    if n == 0: 
     
        break 
    
    L. append(n) 

for i in range(len(L)):
    
    print(L[i], end=" ") 