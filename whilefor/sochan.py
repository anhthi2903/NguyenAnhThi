n=int(input())
if n>=0 and n<=10**6:
    s=0
    for i in range (1,n+1):
        if i%2==0:
            s=s+i
    print(s)