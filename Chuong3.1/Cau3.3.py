x=int(input('Tien thu='))
if x<=100: t=x*550
elif x<=150: t=(100*550)+((x-100)*750)
elif x<=200: t=(100*550)+(50*750)+((x-150)*950)
else: t=(100*550)+(50*750)+(50*950)+((x-200)*1350)
VAT=1.1
print('Phai tra='+str(t*VAT))