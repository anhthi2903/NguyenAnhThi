a=int(input())
b=int(input())
if a<=b and b>0 and a>0:
    for i in range (b-1,a+1,-1):
        if i%3==0:
            print(i, end=' ')
    if a==b:
        print('NOT FOUND')