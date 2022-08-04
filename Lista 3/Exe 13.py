cont = 0
soma = 0
while True:
    n = int(input())
    if(n == -1):
        break
    soma += n
    cont += 1   
media = soma / cont
print(int(media))
