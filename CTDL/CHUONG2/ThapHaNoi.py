# n=int(input('n='))
# A=[]
# # for i in range(0,n+1,7):
# #     A.append(i+1)
# #     A.append(i+2)
# #     A.append(i+4)
# # for i in A:
# #     if i <= n:
# #         print(i)
# while True:
#     for i in range (3):
#         m=2**i
#         if m<=n:
#             print(m)
#             A.append(m)
#         else: break
def F(x):
    if x==1:
        return 1
    elif x==2:
        return 2
    elif x==3:
        return 4
    else : return F(x-3)+7
n=int(input('n='))
for i in range (1,n):
    if F(i) <=n:
        print(F(i),end=' ')
    