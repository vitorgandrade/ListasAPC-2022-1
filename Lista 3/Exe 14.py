a, b = input().split()
a = int(a)
b = int(b)
if(a > b):
    a, b = b, a
while(a > 0):
    resto = b % a
    a, b = resto, a

menordivcomum = b

if(b == 1):
    print('Sao co-primos.')

else:
    print('Nao sao co-primos!')