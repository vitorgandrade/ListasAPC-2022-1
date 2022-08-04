def formamisteriosa(a, b, c):
    if(a == b):
        print('pode ser quadrado')
    if(a != b):
        print('pode ser retangulo')
    if(((a + b) > c) and ((b + c) > a) and ((a + c) > b)):
        if((a != b) and (b != c) and (a != c)):
            print('pode ser triangulo escaleno')
        elif((a == b) and (b == c)):
            print('pode ser triangulo equilatero')
        elif((a == b) or (a == c) or (b == c)):
            print('pode ser triangulo isosceles')