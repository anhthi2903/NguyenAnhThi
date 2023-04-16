# Nhap A,B tính tổng trong khoảng A,B
a=int(input())
b=int(input())
if a<=b and a>0 and b>0:
    # print(((a+b)*(b-a+1))/2)
    s=0
    for i in range (a+1,b):
        s=s+i
    print(s)