def gt(n):
    if n==0: return 1
    return n*gt(n-1)
n=int(input('n='))
k=int(input('k='))

print('To hop chap',k,'cua',n,'la',gt(n)/(gt(k)*gt(n-k)))
print('Chinh hop chap',k,'cua',n,'la',gt(n)/gt(n-k))
print('hoan vi',gt(n))