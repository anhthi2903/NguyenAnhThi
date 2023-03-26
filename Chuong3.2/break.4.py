while True:
    a=float(input('a='))
    b=float(input('b='))
    c=input('c=')
    if c=='+':
        d=a+b
        print(a,c,b,'=',d,sep='')
    elif c=='-':
        d=a-b
        print(a,c,b,'=',d,sep='')
    elif c=='*':
        d=a*b
        print(a,c,b,'=',d,sep='')
    elif b!=0:
        d=a/b
        print(a,c,b,'=',d,sep='')
    c=input('Tiep tuc:')
    if c=='t' or c=='T':
        break