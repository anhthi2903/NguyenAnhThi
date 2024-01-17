def GT(n):
    if n == 0: return 1
    return n *GT(n-1)
n=int(input('n='))
if n<0: print('loi')
else:
    KQ=GT(n)
    print('Tich la',KQ)