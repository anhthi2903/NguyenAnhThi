x=int(input())
a=int(input())
b=int(input())
if x<=100:
    t=0
elif 100<x<=250:
    t=x*25
elif x>250:
    t=(x-25)*20
print(t+a*15+b*20)
print(t+a*35+b*25)