def ortogonais(dimen, vetu, vetv):
    cont = 0
    prodeuclid = 0
    while(cont != dimen):
        prodeuclid += vetu[cont] * vetv[cont]
        cont += 1
    if(prodeuclid == 0):
        resultado = 'ortogonais'
        return resultado
    else:
        resultado = prodeuclid
        return resultado
    
dimen = int(input())
vetu = list(map(int,input().strip().split()))
vetv = list(map(int,input().strip().split()))
resultado = ortogonais(dimen, vetu, vetv)
print(resultado)