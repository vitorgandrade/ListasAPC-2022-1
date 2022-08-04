n = int(input())
s = input()
cont = 0
for i in n:
    if(s[i] < s[i+1]):
        s.append(s[i+1])


