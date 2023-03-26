n=int(input())
for i in range(1,n+1):#dong
    for j in range (n-i,-1,-1):#so khoang trong
        print(' ',end='')
    for k in range(1,2*i):#cot nhung sao chạy theo hàng ngang
        print('*',end='')
    print()