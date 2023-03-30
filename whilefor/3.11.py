n=int(input())
am=0
duong=0
while n!=0:
    if n>0:
        duong=duong+1
    elif n<0:
        am=am+1
    n=int(input())
print(duong,'so duong')
print(am,'so am')