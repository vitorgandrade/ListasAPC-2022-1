def repetir():
    repet1 = str1 * num
    print(repet1)

def concatenar():
  concat1 = str1 + str2
  print(concat1)
  return concat1

def ambos():
    tudo = (str1 + str2) * num
    print(tudo)

str1, str2, num = input().split()
num = int(num)

concatenar()
repetir()
ambos()