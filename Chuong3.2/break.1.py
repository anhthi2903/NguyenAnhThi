#Dung For
n=int(input())
S=1
for i in range (1,n+1):
    S=S*i
print(n,'!=',S,sep='')
#Dung While
n=int(input())
S=1
i=1
while i<=n:
    S=S*i
    i=i+1
print(n,'!=',S,sep='')