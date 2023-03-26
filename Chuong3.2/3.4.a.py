#cach 1
n=int(input('Nhap n='))
i=1
while i<=n:
    j=1#in len man hinh (10-i) dau $
    while j<=(n+1-i):
        print('$',end='')
        j=j+1
    print()
    i=i+1
#cach 2 
n=int(input())
i=n
while i>=1:
    print('$'*i)
    i=i-1