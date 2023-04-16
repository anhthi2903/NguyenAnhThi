def HoanVi(x,y):
    z=x # bien x la cuc bo
    x=y # bien x y la bien cuc bo
    y=z
    return x,y
x=5 # bien x la bien toan bo
y=10
x,y=HoanVi(x,y)
print('x=',x,'y=',y)