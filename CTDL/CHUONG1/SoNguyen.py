a=int(input('a='))
b=int(input('b='))
ch=input()
if ch=='+':
    print(a, '+',b,'=',a+b)
elif ch=='-':
   print(a, '-',b,'=',a-b)
elif ch=='*':
    print(a, '*',b,'=',a*b)
elif ch=='/' :
    if b==0:
        print('Khong hop le')
    else: print(a, '/',b,'=',a/b)
else: print('Khong hop le')