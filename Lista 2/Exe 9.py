def classificador(a, b, c):
    if(((a + b) > c) and ((b + c) > a) and ((a + c) > b)):
        print('triangulo')
        if((a != b) and (b != c) and (a != c)):
            print('escaleno')
        if((a == b) or (a == c) or (b == c)):
            print('isosceles')
        if((a == b) and (b == c)):
            print('equilatero')
        if((a*a + b*b == c*c) or (a*a + c*c == b*b) or (b*b + c*c == a*a)):
            print('retangulo')
    else:
        print('gondim sendo gondim')