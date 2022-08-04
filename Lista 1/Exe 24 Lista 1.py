def resto(a, b, d):
    varResto = (a + b) % d
    print("%d" % varResto)

for i in range(3):
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    resto(a, b, c)