# ktra SNT
def nhap():
    n=int(input())
    return n
def SNT(x):
    if (x%2==0 and x>2): 
        return False
    return True
def ktr(n):
    if SNT(n):
        print(n,'la SNT')
    else: print(n,'khong la SNT')

n=nhap()
ktr(n)