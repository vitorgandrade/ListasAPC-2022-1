tamanho = int(input())
sapatos = list(map(int,input().strip().split()))
tamlista = len(sapatos)
for i in range (tamlista):
    if(tamanho <= min(sapatos)):
        print(sapatos.index(min(sapatos)))
        #break
    elif(tamanho >= max(sapatos)):
        print(-1)
        #break
    elif(tamanho <= sapatos[i]):
        print(sapatos.index(sapatos[i]))
        #break
    else: #(tamanho > sapatos[i]):
        if(tamanho > sapatos[i]):
            print(sapatos.index(sapatos[i]))
            #break
        #else:
    break
