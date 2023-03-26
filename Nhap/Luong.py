ten=input('Ho ten: ')
ngay=int(input('So ngay cong: '))
dongia=int(input('Don gia ngay cong: '))
heso=float(input('He so phu cap: '))
tamung=int(input('Tam ung: '))
luong=dongia*ngay*heso
thuclinh=luong-tamung
print('Nhan vien '+ten+', Co tien Luong='+str(round(luong,1))+', Tam ung='+str(tamung)+' va Thuc linh='+str(round(thuclinh,1)))