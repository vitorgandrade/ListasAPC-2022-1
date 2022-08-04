def testandotam(tamanho, sapatos, tamlista):
    for i in range (tamlista):
        if(tamanho <= min(sapatos)):
            resultado = sapatos.index(min(sapatos))
            return resultado
        elif(tamanho >= max(sapatos)):
            resultado = -1
            return resultado
        elif(tamanho <= sapatos[i]):
            resultado = sapatos.index(sapatos[i])
            return resultado
        else: #(tamanho > sapatos[i]):
            if(tamanho > sapatos[i]):
                testandotam()
            #else:
tamanho = int(input())
sapatos = list(map(int,input().strip().split()))
tamlista = len(sapatos)
testandotam(tamanho, sapatos, tamlista)
resultado = testandotam(tamanho, sapatos, tamlista)  
print(resultado)