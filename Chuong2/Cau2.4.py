a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
import math
s=((a+b+c)/2)
dientich=math.sqrt(s*(s-a)*(s-b)*(s-c))
print('Dien tich='+str(dientich))