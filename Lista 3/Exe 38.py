n = int(input())
for i in range (n):
    s = input()
    cont = 0
    for j in range (len(s)-1):
        if((s[j] == '1') and (s[j + 1] == '0')):
            flag = False
            for k in range (j + 2, len(s)):
                if(s[k] == '1'):
                    flag = True
            if flag:
                for x in range (j+1, s[x]!='1'):
                    cont+= 1
    print(cont)        
