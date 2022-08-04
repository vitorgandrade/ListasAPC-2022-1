from posixpath import split
from re import X


n = int(input())
cont = 0
for i in range (n):
    x, y, z = input().split()
    x, y, z = int(x), int(y), int(z)
    if((X and y == 1) or (x and z == 1) or (y and z == 1)):
        cont += 1   
    else:
        cont += 0
print(cont)