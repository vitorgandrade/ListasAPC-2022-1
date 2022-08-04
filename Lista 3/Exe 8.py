senha = str(input())
tamanho = 0
minuscula = 0
maiuscula = 0
especial = 0
while True:
    if (len(senha) <= 32 and len(senha) >= 6): 
        tamanho = True 
        break
    if(senha.islower()): 
        minuscula = True
        break
    if(senha.isupper()): 
        maiuscula = True
        break
    if((not senha.isalpha()) and (not senha.isnumeric())): 
        especial = True
        break

if(tamanho and minuscula and maiuscula and especial): 
    print("Senha valida.")   
else: 
    print("Senha invalida.")