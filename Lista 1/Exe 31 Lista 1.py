h, m, s = input().split(':')
h = int(h)
m = int(m)
s = int(s)
s += (h * 3600) + (m * 60)
print("La se foram %d segundos que nao voltam mais..." % (s))