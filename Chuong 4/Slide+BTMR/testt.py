def Nhap():
    n=int(input('n='))
    return n
def NhapVaDem(n):
    print('Nhap',n,'so nguyen:')
    s=0
    for i in range (1,n+1):
        a=int(input())
        if a%2==0:
            s=s+1
    return s
def InKQ(kq):
    print('So chu so chan la:',kq)
    return kq
    
n=Nhap()
kq=NhapVaDem(n)
InKQ=InKQ(kq)