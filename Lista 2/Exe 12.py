def jogadas(a, b):
  count = 0
  while (a != b):
    if(a < b):
      if(b - a > 10):
        a = a + 10
        count += 1
      else:
        a = b
        count += 1
    else:
      if(a - b > 10):
        b = b + 10
        count += 1
      else:
        b = a
        count += 1
  print(count)