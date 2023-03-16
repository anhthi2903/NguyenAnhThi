M1=int(input('M1='))
M2=int(input('M2='))
M3=int(input('M3='))
S=int(input('S='))
if S<=100: t=S*M1
elif S<=150: t=((M1*100)+(S-100)*M2)
else : t=((M1*100)+(M2*50)+(S-150)*M3)
print('Phai tra='+str(t))