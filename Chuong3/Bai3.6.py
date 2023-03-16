a=int(input())
b=int(input())
c=int(input())
if (a+b<=c) or (a+c<=b) or (b+c<=a) or (a<=0) or (b<=0) or (c<=0):
    print('Khong hop le')
elif (a==b) and (b==c) and (c==a):
    print('Tam giac deu') 
elif (a*a==b*b+c*c) or (b*b==a*a+c*c) or (c*c==a*a+b*b):
    print('Tam giac vuong')
else:
    print('Tam giac loai khac')