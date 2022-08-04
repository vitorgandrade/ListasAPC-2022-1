cont = 0
soma = 0
while True:
    n = int(input())
    if(n == -1):
        break
    soma += (1 / n)
    cont += 1   
media = cont / soma
print(int(media))