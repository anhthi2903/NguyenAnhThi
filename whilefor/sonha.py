a=int(input('So nha dang o:'))
b=int(input('So nha can den:'))
if a%2==0:
    if b%2==0:
        if b>a:
            c=(b-a)/2 # tìm số nhà cần đi qua hàng chẵn
            print('So nha can di qua la:',c)
            print('so nha can phai di them la:',c)
        elif b<a:
            c=(a-b)/2
            print('So nha can di qua la:',c)
            print('so nha can phai di them la:',c)
    else:
        d=a-1 # chuyển từ số nhà chẵn sang số nhà lẻ cùng hàng
        if b>d:
            c=(b-d)/2 # tìm số nhà cần đi qua bên hàng lẻ
            print('So nha can di qua la:',c)
            print('so nha can phai di them la:',c)
        elif b<d:
            c=(d-b)/2
            print('So nha can di qua la:',c)
            print('so nha can phai di them la:',c)
else:
    if b%2==0:
        d=a+1 # chuyển từ số nhà lẻ sang nhà số chẵn cùng hàng
        if b>d:
            c=(b-d)/2 # tìm số nhà cần đi qua bên hàng chẵn
            print('So nha can di qua la:',c)
            print('so nha can phai di them la:',c)
        elif b<d:
            c=(d-b)/2 #
            print('So nha can di qua la:',c)
            print('so nha can phai di them la:',c)
    else:
        if b>a:
            c=(b-a)/2 # tìm số nhà cần đi qua bên hàng lẻ
            print('So nha can di qua la:',c)
            print('so nha can phai di them la:',c)
        elif b<a:
            c=(a-b)/2
            print('So nha can di qua la:',c)
            print('so nha can phai di them la:',c)