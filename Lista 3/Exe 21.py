n = int(input())
cont = 1
while(cont <= n):
    if((cont % 15 == 0)):
        print('Fizz Buzz')
    else:
        if(cont % 3 == 0):
            print('Fizz')
        else:
            if(cont % 5 == 0):
                print('Buzz')
            else:
                print(cont)
    cont += 1