amigos, ingresso = input().split()
amigos = int(amigos)
ingresso = int(ingresso)
soma = 0
for i in range (amigos):
    valores = int(input())
    soma += valores
media = soma / amigos
print('media: %d' % (media))
if(media > ingresso):
    print('o rock reinara mais uma vez')
else:
    print('rockeiros trabalhando ja')