#Nhap x neu ton tai thi xoa, con lai thi them x vao L
L=[1,2,3,4,3,5]
x=int(input('x='))
i=0
if x in L: #Ton tai thi xoa
    # # del(L[L.index(x)])
    # while x in L:
    #     L.remove(x)
    while L.count(x)>0:
        L.remove(x)
else: L=L+[x] #khong ton tai thi them x vao L
print('Sau khi xu ly:')
print(L)