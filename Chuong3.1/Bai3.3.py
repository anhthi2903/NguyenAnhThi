x=float(input('x='))
y=float(input('y='))
ch=str(input('Phep toan:'))
if ch=='+':
    print(str(x)+str(ch)+str(y)+'='+str(round((x+y),1)))
elif ch=="-":
    print(str(x)+str(ch)+str(y)+'='+str(round((x-y),1)))
elif ch=="*":
    print(str(x)+str(ch)+str(y)+'='+str(round((x*y),1)))
elif ch=="/":
    if y==0:
        print('Khong hop le')
    else:
        print(str(x)+str(ch)+str(y)+'='+str(round((x/y),1)))
else:
    print('Khong hop le')