a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
max=a
min=a
if max<b: max=b
if max<c: max=c
if min>b: min=b
if min>c: min=c
print('SLN=',max,sep='')
print('SNN=',min,sep='')