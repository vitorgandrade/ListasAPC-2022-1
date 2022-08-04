def qtdcopos(n):
    x = n / 4
    if((n % 4 == 0) and (n > 4)):
        print('Pode levar pros calourinhos, deivis!')
    else:
        if(n < 4):
            a = 4 - n
            print("Pode voltar pro ceubinho, deivis! Falta(m) %d copo(s)!" % (a))
        if((n % 4 < 4) and (n > 4)):
            y = n % 4
            z = 4 - y
            print("Pode voltar pro ceubinho, deivis! Falta(m) %d copo(s)!" % (z))