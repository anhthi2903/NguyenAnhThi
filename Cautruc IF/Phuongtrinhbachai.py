import math
print('Nhap a,b,c:')
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
d=b*b-4*a*c #denta
if d<0:
    print('Phuong trinh vo nghiem!!!')
elif d==0:
    print('Phuong trinh co nghiem kep x1,x2=',(-b/2*a))
else:
    print('Phuong trinh co hai nghiem:\n')
    print('x1=',(-b+math.sqrt(d))/(2*a))
    print('x2=',(-b-math.sqrt(d))/(2*a))