# Hàm Nhap(): nhập từ bàn phím một số nguyên n
# Hàm LaSNT(x): trả về True nếu x là SNT, còn lại trả về Fasle
# Hàm InKQ(n): sử dụng hàm LaSNT(x) để kiểm tra n có phải là SNT không , in lên màn hình theo mẫu sau:
# n=7 7 la SNT
def Nhap():
    n=int(input('n='))
    return n
def LaSNT(x):
    for i in range (2,x):
        if x%i==0:
            return False 
        else:
            return True
def InSoNguyenTo(n):
    # if LaSNT(n):
    #     print(n,'la SNT')
    # else: print(n,'khong la SNT')
    for i in range (2,n):
        if LaSNT(i):
            print(i,end=' ')
n=Nhap()
InSoNguyenTo(n)