n=int(input('n='))
for m in range (n,1,-1):
    snt=True
    for i in range (2,m):
        if m%i==0:
            snt=False
            break
    if snt==True:
        print(m,'la snt')
        break