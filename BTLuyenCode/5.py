import math
xA=int(input())
yA=int(input())
xB=int(input())
yB=int(input())
xC=int(input())
yC=int(input())
AB=math.sqrt(((xA-xB)*(xA-xB))+(yA-yB)*(yA-yB))
BC=math.sqrt((xB-xC)*(xB-xC)+(yB-yC)*(yB-yC))
AC=math.sqrt((xA-xC)*(xA-xC)+(yA-yC)*(yA-yC))
p=(AB+BC+AC)/2
s=math.sqrt(p*(p-AB)*(p-BC)*(p-AC))
print(p*2)
print(s)