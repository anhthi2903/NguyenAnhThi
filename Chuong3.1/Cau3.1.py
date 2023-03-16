a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
if a>b and a>c:
    print('SLN='+str(a))
elif b>a and b>c:
    print('SLN='+str(b))
else:
    print('SLN='+str(c))
if a<b and a<c:
    print('SNN='+str(a))
elif b<a and b<c:
    print('SNN='+str(b))
else:
    print('SNN='+str(c))