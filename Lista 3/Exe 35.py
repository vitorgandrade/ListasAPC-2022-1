n = str(input())
Listan = list(n)
inverson = list(reversed(Listan))
if(not inverson[len(inverson) - 1].isalnum()):
    inverson.insert(0, '-')
    inverson.pop(len(inverson)-1)
novon = ''.join(inverson)
print(novon)
