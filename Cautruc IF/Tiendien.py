tieuthu=int(input('Tieu thu='))
VAT=0.1
if tieuthu<=100:
    t=tieuthu*550
elif tieuthu <=150:
    t=(100*550)+((tieuthu-100)*750)
elif tieuthu<=200:
    t=(100*550)+(50*750)+((tieuthu-150)*950)
else: 
    t=(100*550)+(50*750)+(50*950)+((tieuthu-200)*1350)
print('Phai tra=',t*VAT+t,sep='')