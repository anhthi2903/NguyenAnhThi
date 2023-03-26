n=int(input('Nhap n='))
i=1
while i<=n:
    j=1
    while j<=(n-i):
        print(' ',end='')
        j=j+1
    k=1
    while k<=(2*i-1):
        print('*',end='')
        k=k+1
    print()
    i=i+1
#cach khac
i=1
n=int(input())
while i<=n:
    #in len man hinh n-i dau cach
    print(' '*(n-i),end='')
    print('*'*(2*i-1))
    i=i+1