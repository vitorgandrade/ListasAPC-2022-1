n = int(input())
for i in range (n + 1):
    #if(i == 1):
        #print('%d elefante incomoda muita gente...' % (i))
        #print('%d elefantes incomodam, incomodam muito mais...' % (i + 1))
    if((i <= 3) and (i > 0)):
        if(i == 1):
            print('%d elefante incomoda muita gente...' % (i))
            print('%d elefantes incomodam, incomodam muito mais...' % (i + 1))
        elif(i == 2):
            print('%d elefantes incomodam muita gente...' % (i))
            print('%d elefantes incomodam, incomodam, incomodam muito mais...' % (i + 1))
            #print('%d elefantes incomodam, incomodam, incomodam muito mais...' % (i + 1))
        else:
            print('%d elefantes incomodam muita gente...' % (i))
    elif(i > 3):
        cont = i
        novoi = i -1
        print(str(cont) + " elefantes " + (novoi*'incomodam, ') + 'incomodam muito mais...')
        print('%d elefantes incomodam muita gente...' % (cont))
if((i != 1) and (i != 2)):
    print(str(i + 1) + " elefantes " + (i*'incomodam, ')+ 'incomodam muito mais...')