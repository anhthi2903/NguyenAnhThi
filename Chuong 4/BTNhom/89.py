# Sửa đổi chữ viết thường thành chữ viết hoa: Đầu câu, đứng sau '.','!','?', chữ'i' khi đứng một mình
n=input()
n=n.title() # phương thức method . title viết hoa đầu câu
for i in range (len(n)):
    if n[i]=='i':
        n[i]=='I'
    if n[i]=='.' or n[i]=='!' or n[i]=='?':
        n[i+2]==n[i+2].upper()
print(n)