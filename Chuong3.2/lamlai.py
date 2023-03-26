n=int(input())
SNT=True
for i in range (2,n):
    if n%i==0:
        SNT=False
        break
if  SNT==True:
    print(n,'la SNT')
else:
    print(n,'khong la SNT')