# #while
n=int(input())
while n>=0:
    i=1
    s=1
    while i<=n:
        s=s*i
        i=i+1
    print(s)
    n=int(input())
 #for
n=int(input())
while n>=0:
    s=1
    for i in range (1,n+1):
        s=s*i
    print(s)
    n=int(input())