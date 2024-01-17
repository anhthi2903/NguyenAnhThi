n=int(input('n='))
if n<=0:
    print('Nhap so nguyen duong')
if n==1 or n==2:
    print(1)
else:
    soThuNhat, soThuHai =1,1
    for i in range (n-2):
        soThuNhat, soThuHai = soThuHai, soThuNhat +soThuHai
        print(soThuNhat)