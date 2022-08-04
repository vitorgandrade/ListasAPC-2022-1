def age(x):
    ano = 0
    mes = 0
    dia = 0
    if(x / 360 >= 1):
        ano = x //  360
        x = x % 360
    if(x / 30 >= 1):
        mes = x // 30
        x = x % 30
    dia = x 
    print("%d ano(s), %d mes(es) e %d dia(s)" % (ano, mes, dia))

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
age(a)
age(b)
age(c)