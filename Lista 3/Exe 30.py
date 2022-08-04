n = int(input())
lista = []
for i in range (n):
    x = int(input())
    lista.append(x)
maiorvalor = max(lista)
menorvalor = min(lista)
print('Menor: %d' % (menorvalor))
print('Maior: %d' % (maiorvalor))