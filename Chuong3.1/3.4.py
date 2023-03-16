num=int(input())
if num<1 or num>12:
    print('Khong hop le')
elif num==1 or num==3 or num==5 or num==7 or num==8 or num==10 or num==12:
    print('31 days')
elif num==2:
    print('28 or 29 days')
else:
    print('30 days')