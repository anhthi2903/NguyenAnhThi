x=float(input('x='))
y=float(input('y='))
ch=input('Phep toan:')
if ch=='+':
    print(str(x)+str(ch)+str(y)+'='+str(x+y))
elif ch=='-':
    print(str(x)+str(ch)+str(y)+'='+str(x-y))
elif ch=='*':
    print(str(x)+str(ch)+str(y)+'='+str
          (x*y))
elif ch=='/':
    if y==0:
        print('Khong hop le')
    else:
        print(str(x)+str(ch)+str(y)+'='+str(x/y))
else:
    print('Khong hop le')