def tempovoltas(voltas, N):
    maiortempo = max(N)
    maiortempo = int(maiortempo)
    cont = 0
    while(cont != voltas):
        novoN = [maiortempo - x for x in N]
        cont += 1
    print(*novoN)
voltas = int(input())    
N = list(map(int,input().strip().split()))
tempovoltas(voltas, N)