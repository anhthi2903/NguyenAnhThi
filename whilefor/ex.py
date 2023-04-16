a=int(input('So nha dang o:'))
b=int(input('So nha can den:'))
if a%2==0:
    if b%2==0:
        c=(a-b)//2
        if c<0:
            print('So nha can tien them la:',abs(c))
        else: print('So nha can lui di la :',abs(c))
    elif b==(a-1):
        print('Chi can qua duong')
    elif b%2!=0:
        d=b+1
        c=(a-d)//2
        if c<0:
            print('So nha can di qua la:',abs(c))
            print('So nha can tien them la:',abs(c))
        else:
            print('So nha can di qua la:',abs(c)) 
            print('So nha can lui di la :',abs(c))
else:
    if b==a+1:
        print('Chi can qua duong')
    elif b%2==0:
        d=b-1
        c=(d-a)//2
        if c>0:
            print('So nha can di qua la:',abs(c))
            print('So nha can tien them la:',abs(c))
        else:
            print('So nha can di qua la:',abs(c)) 
            print('So nha can lui di la :',abs(c))
    elif b%2!=0:
        c=(a-b)//2
        if c<0:
            print('So nha can tien them la:',abs(c))
        else: print('So nha can lui di la :',abs(c))