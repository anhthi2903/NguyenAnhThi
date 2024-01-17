import math
n=int(input(('Nhap so nguyen duong n: ')))

def snt(n):
    if n<2:
        return False
    if n==2 or n==3:
        return True
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
    
for i in range (2, n+1):    
    if snt(int(i)) == True:
        print(i)
    