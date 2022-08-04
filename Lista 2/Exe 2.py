def area(arg1, arg2, forma):
    if(forma == 'losango'):
        a = (arg1 * arg2) / 2
        print("O %s tem %d de area" % (forma, a))
    if(forma == 'retangulo'):
        a = arg1 * arg2
        print("O %s tem %d de area" % (forma, a))
    if(forma == 'triangulo'):
        a = (arg1 * arg2) / 2
        print("O %s tem %d de area" % (forma, a))