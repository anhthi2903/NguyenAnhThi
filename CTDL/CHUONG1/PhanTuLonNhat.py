# def Nhap(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# def Phanso(tu1, mau1, tu2, mau2):
#     tu = tu1 * mau2 + tu2 * mau1
#     mau = tu1 * mau2
    
#     USC = Nhap(tu, mau)

#     tu //= USC
#     mau //= USC
    
#     return tu , mau

# def inkp():
            
#         tuso1 = int(input("Nhập tự số của phân số thứ nhất: "))
#         mauso1=int(input("Nhập mẫu số của phân  số thứ nhất:"))
#         tuso2 = int(input("Nhập tử số của phân số thứ hai: "))
#         mauso2 = int(input("Nhập mẫu số của phân số thứ hai: "))
        
#         ketquatu, ketquamau =Phanso(tuso1, mauso1, tuso2, mauso2)
#         if mauso1!=0 or mauso2!=0:
#             print("Ket qua:", ketquatu, "/", ketquamau)
#         else: print('Khong hop le')
        
# inkp()
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
d=int(input('d='))
if b==0 or d==0:
    print('Khong hop le')
elif b==d:
    pheptinh=(a+c)/d
    print(pheptinh)
else: 
    pheptinh=((a*d)+(b*c))/(b*d) 
    # tìm một ước chung lớn nhất
    print(pheptinh)