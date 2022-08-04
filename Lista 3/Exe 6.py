def tempovoltas(voltas, N):
    menortempo = min(N)
    menortempo = int(menortempo)
    cont = 0
    while(cont != voltas):
        novoN = [x-menortempo for x in N]
        cont += 1
    print(*novoN)
voltas = int(input())    
N = list(map(int,input().strip().split()))
tempovoltas(voltas, N)