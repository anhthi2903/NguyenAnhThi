cho=int(input())
nguoi=0
if cho<0:
    print('Khong hop le')
elif cho<=2:
    print(cho*10.5)
elif cho>=3:
    print((2*10.5)+(cho-2)*4)