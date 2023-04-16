a=int(input())
b=int(input())
c=int(input())
if a==0 and b==0:
    print('NO')
elif b==0:
    print('INF')
else:
    print(round(-b/a,2))