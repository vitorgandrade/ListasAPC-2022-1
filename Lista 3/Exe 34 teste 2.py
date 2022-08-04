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

tamanho = int(input())
sapatos = list(map(int,input().strip().split()))
sapatos.sort()
#print(sapatos)
tamlista = len(sapatos)
resultado = testandotam(tamanho, sapatos, tamlista)
print(resultado)