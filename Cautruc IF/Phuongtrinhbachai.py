import math
print('Nhap a,b,c:')
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
d=b*b-4*a*c #denta
if a==0:
    if b!=0:
        print('Phuong trinh co mot nghiem:','x=',-c/b)
    elif b==0 and c!=0:
        print('Phuong trinh vo nghiem')
    elif b==0 and c==0:
        print('Phuong trinh vo so nghiem')
else: 
    if d<0:
        print('Phuong trinh vo nghiem!!!')
    elif d==0:
        print('Phuong trinh co nghiem kep x1,x2=',(-b/2*a))
    else:
        print('Phuong trinh co hai nghiem:\n')
        print('x1=',round((-b+math.sqrt(d))/(2*a),2))
        print('x2=',(-b-math.sqrt(d))/(2*a))