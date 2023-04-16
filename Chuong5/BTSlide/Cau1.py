def add(L,x,k):
    if k > len(L):
        L=L+[k]
    elif k<= 0:
        L=[x]+L
    else: 
        L=L[:k-1] +[x]+ L[k-1:]
    return L
L=[1,2,3,4,5,6,7]
x=15
k=3
L=add(L,x,k)
print(L)