def Nhap():
    n=int(input('n='))
    return n # can tra ket qua lai cho ham , neu khong thi khong ra n
def NhapVaDem(n):
    print('Nhap',n,'so nguyen:')
    dem=0
    for i in range (1,n+1):
        x=int(input())
        if x%2==0 and x!=0:
            if x==0:
                continue
            else:
                dem=dem+1
    return dem # neu khong return dem thi khong lay duoc so luong so chan da nhap vao
def InKQ(kq): # kq chinh la gia tri bien dem
    print('So chu so chan la:',kq)
# ko can return ham InKQ vì khong can tra ket qua lai cho ham
n=Nhap()
kq=NhapVaDem(n) #n là đầu vào của hàm Nhap
InKQ(kq)# kq là đầu ra của hàm NhapVaDem và đầu vào của hàm InKQ
#kiemthu
#1: n=Nhap()
#   print(n)
#2: che hàm nhập 
# dem=NhapVaDem(5) nhập 5 số nguyên
#   print(dem)
#3: InKQ(10) => chạy