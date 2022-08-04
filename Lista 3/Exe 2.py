def soma_harmonica(x):
    if(x == 1):
        return 1
    elif(x > 1):
        return ((1/x) + soma_harmonica(x-1))
    else:
        return 0

a = int(input())
soma_h = soma_harmonica(a)
print(soma_h)