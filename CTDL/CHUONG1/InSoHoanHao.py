import time
def so_hoan_hao(n):
    sum=0
    for i in range (1,n):
        if n%i==0:
            sum=sum+i
    if sum==n:
        return True 
    return False


n=int(input('nhap n:'))
start_time=time.time()
for i in range (1,n+1):
    if so_hoan_hao(i) == True:
        print(i)
end_time=time.time()  
total_time=end_time-start_time
print(total_time)

def so_hoan_hao(n):
    sum=0
    for i in range (1,int((n/2)+1)):
        if n%i==0:
            sum=sum+i
    if sum==n:
        return True 
    return False


n=int(input('nhap n:'))
start_time=time.time()
for i in range (1,n+1):
    if so_hoan_hao(i) == True:
        print(i)
end_time=time.time()  
total_time=end_time-start_time
print(total_time)

    

def so_hoan_hao(n):
    sum=0
    if n%2==0:
        for i in range (1,int((n/2)+1)):
            if n%i==0:
                sum=sum+i
    else:
        for i in range (1,int((n/3)+1)):
            if n%i==0:
                sum=sum+i
    if sum==n:
        return True 
    return False


n=int(input('nhap n:'))
start_time=time.time()
for i in range (1,n+1):
    if so_hoan_hao(i) == True:
        print(i)
end_time=time.time()  
total_time=end_time-start_time
print(total_time)