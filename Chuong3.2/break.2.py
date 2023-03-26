n=int(input())
SNT=True
for i in range (2,n):#(2,math.sqrt(n)+1)
    if n%i==0:
        SNT=False
        break
if  SNT==True:
    print(n,'la SNT')
else:
    print(n,'khong la SNT')
#dung while