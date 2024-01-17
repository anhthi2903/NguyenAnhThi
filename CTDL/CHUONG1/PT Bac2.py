import math
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
dt=b*b-4*a*c
if dt<0:
    print('Phuong trinh vo nghiem')
elif dt==0:
    print('Phuong trinh co nghiem kep x1, x2=',(-b/2*a))
else:
    print('Phuong trinh co hai nghiem:')
    print('x1=',(-b + math.sqrt(dt))/(2*a))
    print('x2=',(-b - math.sqrt(dt))/(2*a))
    