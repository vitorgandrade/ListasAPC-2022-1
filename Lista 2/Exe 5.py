def dinheiros(n, a, b):
    if((a * n) < ((n / 2) * b)):
        print("%d" % (a * n))
    else:
        print("%d" % ((n / 2) * b))

def dinheiros(n, a, b):
  if((n % 2) == 0):
    if(a <= (b/2)):
      print(int(a*n))
    else:
      print(int(b*n/2))
  else:
    if(n == 1):
      print(int(a))
    else:
      n -= 1
      if(a <= (b/2)):
        print(int(a*(n+1)))
      else:
        print(int((b*n/2)+(a)))



def dinheiros(n, a, b):
  if((n % 2) == 0):
    if(a <= (b/2)):
      print(int(a*n))
    else:
      print(int(b*n/2))
  else:
    if(n == 1):
      print(int(a))
    else:
      n -= 1
      if(a <= (b/2)):
        print(int(a*(n+1)))
      else:
        print(int((b*n/2)+(a)))