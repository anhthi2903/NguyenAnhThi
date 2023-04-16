def nhap():
    n=int(input('n='))
    return n
def LaSNT(x):
    for i in range (2,x):
        if x%i==0:
            return False
    return True
# def InKQ(n):
#     for i in range (2,n):
#         if LaSNT(i):
#             print(i,end='')
def InKQ(n):
    dem=0
    k=2
    while dem<n:
        if LaSNT(k)==True:
            print(k,end='')
        dem=dem+1
    k=k+1
            
n=nhap()
InKQ(n)