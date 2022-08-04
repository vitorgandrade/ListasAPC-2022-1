def permuta(a):
    cont = 0
    n = len(a)
    for i in range(n -1):
        for j in range(n - i - 1):
            if(a[j] > a[j + 1]):
                a[j], a[j+1] = a[j + 1], a[j]
                cont += 1
    print(cont)            
    
a = list(map(int,input().strip().split()))
permuta(a)