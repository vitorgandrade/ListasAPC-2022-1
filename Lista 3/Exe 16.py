pop = int(input())
soma = 0
for i in range (pop):
    dinheiro = int(input())
    if(dinheiro < 1000):
        diferença = 1000 - dinheiro
    else:
        diferença = 0
    soma += diferença
print(soma)