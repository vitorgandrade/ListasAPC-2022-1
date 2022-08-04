def maravilhosos(x):
    print(x)
    while(x != 1):
        if(x % 2 == 0):
            x = x/2
            print(int(x))
        else:
            x = 3 * x + 1
            print(int(x))

x = int(input())
maravilhosos(x)