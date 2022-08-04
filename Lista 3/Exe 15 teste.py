popA, popB, crescA, crescB = input().split()
popA = int(popA)
popB = int(popB)
crescA = float(crescA) / 100
crescB = float(crescB) / 100
if(popA > popB):
    print('A nunca alcancara B.')
elif(popA * crescA == 0):
    print('A nunca alcancara B.')
else:
    anos = 0
    flag = False
    while(popA < popB):
        popA += int(popA * crescA)
        popB += int(popB * crescB)
        anos += 1
        if(anos == 1000):
            flag = True
            break
    if(flag):
        print('Mais de um milenio')
        print(anos)
    else:
        print('Vai alcancar em %d ano(s).' % (anos))