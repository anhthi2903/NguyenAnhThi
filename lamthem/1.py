n=int(input())
S=0
dem=1
while n>0:
    S=S+n
    n=int(input()) 
    if n==0:
        break   
    dem=dem+1
print(S/dem)