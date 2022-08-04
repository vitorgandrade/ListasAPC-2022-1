cot = float(input())
valor = int(input())
quantlotes = int(input())
valorcorrigido = valor + (valor * 0.025)
valortotal = cot * valorcorrigido
count = 1
for i in range (quantlotes):
    print('Lote: %d - Total da venda: R$ %.2f' % (count, valortotal))
    count += 1