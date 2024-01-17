import math
import time
bd=time.time()
def SNT(n):
    if (n<2):
        return False
    for i in range (2,int(math.sqrt(n))+1):
        if (n%1 == 0):
            return False
    return True
n=int(input("nhap so n: "))
print("so nguyen to tu 1 den n la:")
if n>=2:
    print('2')
for i in range(3, n + 1):
    if SNT(i) == True:
        print(i)
kt=time.time()
tg=kt-bd
print(tg)
