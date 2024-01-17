import math
import time
bd=time.time()
def SNT(n):
    if (n==2):
        print(n)
    else: 
        s=0
        for i in range (2,int(math.sqrt(n)+1)):
            if (n%i==0):
                s=s+1
        if (s==0):
            print(n)
        SNT(n-1)
n=int(input("Nhập n:"))
print("Các số nguyên tố nhỏ hơn",n,"là:")
SNT (n-1)
kt = time.time()
tg = kt-bd
print(tg)
