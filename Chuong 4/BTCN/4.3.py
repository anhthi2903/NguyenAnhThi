import math
def nhap():
    a = int(input('a='))
    b = int(input('b='))
    c = int(input('c='))
    return a, b, c
def giaipt(a, b, c):
    d = b*b - 4*a*c
    if a!=0 and b!=0 and c!=0:
        if d>0:
            print('Phuong trinh co hai nghiem')
            x1 = (-b + math.sqrt(d))/(2*a)
            x2 = (-b - math.sqrt(d))/(2*a)
        elif d==0:
            print('Phuong trinh co nghiem kep')
            x1 = (-b + math.sqrt(d))/(2*a)
            x2 = (-b - math.sqrt(d))/(2*a)
        elif d<0:
            print('Phuong trinh vo nghiem')
            x1=None
            x2=None
    return d,x1,x2
def inkq(d,x1,x2):
    if d>0 and x1!=x2:
        print('x1=',x1,sep='')
        print('x2=',x2,sep='')
    elif d==0 and x1==x2:
        print('x1=x2=',x1,sep='')
    elif d<0:
        print()
print('Nhap 3 so nguyen:')
a, b, c = nhap()
d,x1,x2=giaipt(a,b,c)
inkq(d,x1,x2)