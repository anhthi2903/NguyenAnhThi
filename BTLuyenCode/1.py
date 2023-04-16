# trung binh
# n=int(input())
# S=0
# dem=1
# while n>0:
#     S=S+n
#     n=int(input()) 
#     if n==0:
#         break   
#     dem=dem+1
# print(S/dem)
# dao nguoc ki tu
n=int(input())
s=0
while n>0:
    s=s*10
    s=s+n%10
    n=n//10
print(s)