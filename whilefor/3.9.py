#while
n=int(input())
i=2
if 2<=n<=50:
    while (i<=n):
        print(i,end=' ')
        i+=2
#for
n=int(input())
for i in range (2,n+1,2):
    print(i,end=' ')