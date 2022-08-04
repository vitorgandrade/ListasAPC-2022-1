cont = 0
n = list(map(int,input().strip().split()))
while True:
    if(n[cont] < 0):
        break    
    cont += 1
    #if(n[cont] < 0):
        #break
novoN = list(reversed(n))
del novoN[0]
print(*novoN)