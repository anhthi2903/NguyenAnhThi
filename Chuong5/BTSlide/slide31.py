def Nhap():
    L=[]
    print("Moi nhap 10 so nguyen:")
    for i in range(10):
        L=L+[int(input())]
    x=int(input("Nhap so nguyen x="))
    return L,x
def InKQ(L):
    for x in L:
        print(x,end=", ")
       
def CauA(L,x):
    # Tim va thay the
    for i in range(len(L)):
        if L[i]==5:
            L[i]=x
    InKQ(L)
   
def CauB(L,x):
    i=0 #So chi muc
    while i<len(L):
        if L[i]==x:
            del(L[i])
        else:
            i+=1
           
    print("\nSau khi xoa x khoi tap L:")
    InKQ(L)
   
L,x=Nhap()
CauA(L,x)
CauB(L,x)
