# Ham Nhap(): Nhập từ bàn phím một số nguyên n
# Ham LaSoDuong(x): hàm kiểm tra số nguyên x, nếu x<=0 thì trả về 0, còn lại trả về 1
# Ham Xuly(n): Nhập từ bàn phím n số nguyên, trả về số lượng số nguyên dương và chẵn, yêu cầu sử dụng hàm LaSoDuong(x) để kiểm đếm
# Ham InKQ(soluong): In lên màn hình giá trị biến soluong, theo mẫu: Co<soluong> so nguyen duong va chan
def Nhap():
    n=int(input())
    return n
def LaSoDuong(x):
    if x>0 and x%2==0:
        return 1
    else: return 0
def Xuly(n):
    s=0
    for i in range (1,n+1):
        x=int(input())
        if LaSoDuong(x)==1:
            s=s+1
    return s
def InKQ(soluong):
    print('Co',soluong,'so nguyen duong va chan')

n=Nhap()
soluong=Xuly(n)
InKQ(soluong)