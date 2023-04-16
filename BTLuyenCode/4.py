# nhap n lien tuc dung lai khi bang 0, in ra SLN và SNN 
n=int(input())
max=n
min=n
while n>0:
    n=int(input())
    if n==0:
        break
    if n>max:
        max=n
    if n<min:
        min=n
print('sln',max)
print('snn',min)