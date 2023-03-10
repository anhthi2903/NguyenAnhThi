import math
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
p=(a+b+c)/2
s=math.sqrt(p*(p-a)*(p-b)*(p-c))
if s>0:
    print('Dien tich='+str(round(s,3)))
else:
    print('Khong hop le')