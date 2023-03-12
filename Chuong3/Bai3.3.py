x=int(input('x='))
y=int(input('y='))
pheptoan=str(input('Phep toan:'))
if pheptoan =='+':
    print(x+y)
elif pheptoan =="-":
    print(x-y)
elif pheptoan =="*":
    print(x*y)
elif pheptoan =="/":
    if y==0:
        print('Khong hop le')
    else:
        print(x/y)
else:
    print('Khong hop le')