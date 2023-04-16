def delete(L,x):
    i=0
    while i<len(L):
        if x==L[i]:
            L=L[:i]+L[i+1:]
        else: i=i+1
    return L
L=[1,2,3,4,5,3,4]
x=4
L=delete(L,x)
print(L)