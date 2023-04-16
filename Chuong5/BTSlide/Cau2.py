def search(L,x):
    for i in range (len(L)):
        if x==L[i]:
            return i
    return None
L=[1,2,3,4,5]
x=2
print(search(L,x))