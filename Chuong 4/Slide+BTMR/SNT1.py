def Nhap():
    n=int(input('n='))
    return n
def LaSNT(x):
    for i in range (2,x):
        if x%i==0:
            return False
    return True
def InSoNguyenTo(n):
    for i in range (2,n+1):
        if LaSNT(i):
            print(i, end=' ')

n=Nhap()
InSoNguyenTo(n)