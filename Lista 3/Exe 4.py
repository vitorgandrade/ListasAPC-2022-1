def notas(nalunos):
    cont = 0
    
    for i in range(nalunos): 
        s1, s2, s3 = input().split()
        s1 = float(s1)
        s2 = float(s2)
        s3 = float(s3)
        notasprovas = s1 + s2 + s3
        mediafinal = notasprovas / 3
        if(mediafinal >= 7):
            print('O ALUNO %d FOI APROVADO' % (cont))
            cont += 1
        else:
            print('O ALUNO %d FOI REPROVADO' % (cont))
            cont += 1
    
nalunos = int(input())
notas(nalunos)