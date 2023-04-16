n=int(input())
# if 0<=n<=10**6:
#     dem=0
#     for i in range (1,n+1):
#         if i%3==0 and i%5==0:
#             dem=dem+1
#     print(dem)
s=0
while n>0:
    n=int(input())
    if n%3==0 and n%5==0:
        s=s+1
print(s)
    
    