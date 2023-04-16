a=int(input())
b=int(input())
c=int(input())
while a>0 and b>0 and c>0:
    if (a+b>c) and (a+c>b) and (b+c>a):
        print('YES')
        break
    else: print('NO')
    a=int(input())
    b=int(input())
    c=int(input())
