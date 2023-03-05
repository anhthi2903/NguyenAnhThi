import math 
print('Nhap vao hai canh cua goc vuong')
a=int(input())
b=int(input())
c=math.sqrt(a*a+b*b)
print('Canh ke thu nhat la: '+str(a)+ ', canh ke thu hai: '+str(b) +',co canh huyen = '+str(round(c,2)))