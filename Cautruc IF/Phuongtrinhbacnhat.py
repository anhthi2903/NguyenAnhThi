#Phuong trinh ax+b
a=int(input('a='))
b=int(input('b='))
if a==0:
    if b==0:
        print('Phuong trinh vo so nghiem!!!')
    else:
        print('Phuong trinh vo nghiem!!!')
else:
    print('Phuong trinh co nghiem x=',(-b/a))