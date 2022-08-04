n = int(input())
x = 0
for i in range (n):
    comandos = str(input())
    if((comandos == 'X++') or (comandos == '++X')):
        x += 1
    if((comandos == 'X--') or (comandos == '--X')):
        x -= 1
print(x)