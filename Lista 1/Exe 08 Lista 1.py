def trocarAB(a, b):
    print("%d %d" % (b, a))
    
for i in range(5):
    a, b = input().split()
    a = int(a)
    b = int(b)
    trocarAB(a, b)