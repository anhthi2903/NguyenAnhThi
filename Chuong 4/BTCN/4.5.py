print('Nhap day so:')
def LaSoNguyenTo(x):
    for i in range (2,x):
        if x%i==0:
            return False
    return True
def SoHopLe(x):
    if x<=1:
        return True
    return False
def NhapVaDem():
    s=0
    while True:
        x=int(input())
        if SoHopLe(x):
            break
        if LaSoNguyenTo(x):
            s=s+1
    return s
def InKQ(kq):
    print('Co',kq,'so nguyen to')

kq=NhapVaDem()
InKQ(kq)