n=int(input())
if 0<=n<=9999:
    print(n,'co',len(str(n)),'chu so')
#cach khac
n=int(input())
d=0
s=n
while n>0:
    n//10==0
    d=d+1
    print(s,'co',d,'chu so')
print()
#cach khac 2
n=int(input())
if n!=0:
    dem=0
    while n>0:
        n=int