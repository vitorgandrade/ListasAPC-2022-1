senha = str(input())
quantcarac = len(senha)
contminuscula = 0
contmaiuscula = 0
contespecial = 0

for i in range (quantcarac):   
    if(senha[i].islower()):
        contminuscula += 1
    if(senha[i].isupper()): 
        contmaiuscula += 1
    if((not senha[i].isalpha()) and (not senha[i].isnumeric())): 
        contespecial += 1

if((quantcarac <= 32 and quantcarac >= 6) and (contminuscula > 0) and (contmaiuscula > 0) and (contespecial == 0)): 
    print("Senha valida.")   
else: 
    print("Senha invalida.")