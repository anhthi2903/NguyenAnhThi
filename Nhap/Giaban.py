gia=int(input('Nhap Gia niem yet: '))
ck=int(input('Nhap Chiet khau: '))
VAT=(gia-ck)*0.01
giaban=gia-ck+VAT
print('Gia ban:',giaban)