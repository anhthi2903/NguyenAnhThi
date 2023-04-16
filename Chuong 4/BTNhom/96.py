# Viết một hàm với chức năng đánh giá xem thử một mật khẩu là tốt hay không 
# (Điều kiện để một mật khẩu được đánh giá là tốt : 
# phải có ít nhât 8 ký tự, chứa ít nhất một chữ viết hoa và một chữ viết thường và một chữ số). 
# Hàm trả về kết quả là True nếu tất cả điểu kiện trên được đáp ứng và nếu không thì sẽ trả về False.

pwd=input()
def matkhau(pwd):
    chuhoa=False
    chuthuong=False
    so=False
    for x in pwd:
        if x>='A' and x<='Z':
            chuhoa=True
        elif x>='a' and x<='z':
            chuthuong=True
        elif x>='0' and x<='9':
            so=True
    if len(pwd)>=8 and chuhoa and chuthuong and so:
        return True
    else: return False
print(matkhau(pwd))