m(n * k)def pacotesDeBolacha(m, n, k):
    while(m < (n*k)):
        k = k-1
    if(m >= (n * k)):
        resultado = n * k
        print("%d" % (resultado))
    resto = m % (n * k) 
    print("%d" % (resto))
        