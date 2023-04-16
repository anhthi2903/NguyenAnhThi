# tìm SNT lớn hơn gần số vừa nhập
def nhap():
    n=int(input())
    return n
def xuly(x):
    for i in range (2,x):
        if x%i==0:
            return False
    return True
def nextprime(n):
    i=n+1
    while n>0:
        if xuly(i):
            break
        i=i+1
    return i
def inkq(kq):
    print(kq)

n=nhap()
kq=nextprime(n)
inkq(kq)