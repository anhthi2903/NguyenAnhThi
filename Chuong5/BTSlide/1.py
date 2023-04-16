L=[]
print('nhap day so:')
while True:
    x=int(input())
    L=L+[x]
    if x==0:
        break
n=int(input('n='))
if n in L:
    print(n,'co ton tai')
else:print(n,'khong ton tai')
# nhap tu ban phim mot so nguyen x, neu x ton tai trong trong tap L thi
# thuc hien xoa x khoii tap L
L=[1,2,3,4,5]
x=int(input('x='))
i=0
#if x in L: neu x ton tai thi xoa
while i<len(L):
    if L[i]==x:
        del(L[i])
    i=i+1
else: #ko ton tai thi them x vào L
    #L=L+[x]
    print('Sau khi xoa:')
print(L)