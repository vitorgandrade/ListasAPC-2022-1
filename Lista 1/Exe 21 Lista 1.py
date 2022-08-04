def print_rectangle(a):
    retangld = '+' * a
    retangmd = '+' + ((a - 2) * ' ') + '+'
    print(a)
    print(retangld)
    print(retangmd)
    print(retangld)

a, b, c = input().split()
a = int(a)
b = int(b) 
c = int(c)

print_rectangle(a)
print_rectangle(b)
print_rectangle(c)