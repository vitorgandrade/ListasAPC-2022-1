n = int(input())
a, b, c = 0, 0, 0
for i in range (n):
    x, y, z = input().split()
    x, y, z = int(x), int(y), int(z)
    a += x
    b += y
    c += z
if((a != 0) or (b != 0) or (c != 0)):
    print('NO')
else:
    print('YES')
