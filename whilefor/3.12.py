# n=int(input())
# s=str()
# if n==0:
#     s='A'
# else:
#     while n>0:
#         if n%10==0:
#             s='A'+s
#         elif n%10==1:
#             s='B'+s
#         elif n%10==2:
#             s='C'+s  
#         elif n%10==3:
#             s='D'+s
#         elif n%10==4:
#             s='E'+s
#         elif n%10==5:
#             s='F'+s
#         elif n%10==6:
#             s='G'+s
#         elif n%10==7:
#             s='H'+s
#         elif n%10==8:
#             s='K'+s
#         elif n%10==9:
#             s='L'+s
#         n=n//10
# print(s)

# n=int(input(''))
# kq=''
# if n==0: kq='A'+kq
# while n>0:
#     z=n%10
#     if (z<=7):
#         kq=(chr(ord('A')+z))+kq
#     if (z==8):
#         kq='K'+z
#     if (z==9):
#         kq='L'+z
#     n//=10
# print(kq)
n=str(input())
s=""
for i in n :
    if i=="0":
        s=s+"A"
    elif i=="1":
        s=s+"B"
    elif i=="2":
        s=s+"C"
    elif i=="3":
        s=s+"D"
    elif i=="4":
        s=s+"E"
    elif i=="5":
        s=s+"F"
    elif i=="6":
        s=s+"G"
    elif i=="7":
        s=s+"H"
    elif i=="8":
        s=s+"K"
    elif i=="9":
        s=s+"L"
print(s)