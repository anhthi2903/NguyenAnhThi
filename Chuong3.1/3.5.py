num=int(input())
if num<0:
    print('Khong hop le')
elif num==130:
    print('Jackhammer')
elif num==106:
    print('Gas lawnmower')
elif num==70:
    print('Alarm clock')
elif num==40:
    print('Quiet room')
elif 40<num<70:
    print('between Quiet room and Alarm clock')
elif 70<num<106:
    print('between Alarm clock and Gas lawnmower')
elif 106<num<130:
    print('between Gas lawnmower and Jackhammer')
elif num<40:
    print('A value smaller than the Alarm clock')
else:
    print('a value larger than Jackhammer')