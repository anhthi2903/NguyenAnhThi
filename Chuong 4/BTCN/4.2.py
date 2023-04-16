def nhap():
    n=int(input('n='))
    return n
def inkq(n):
    while True:
        for i in range (2,n+1,2):
            print(i,end=' ')
        c=input('\nTiep tuc khong?')
        if c=='k' or c=='K':
            break
        n=int(input('n='))
        
n=nhap()
inkq(n)