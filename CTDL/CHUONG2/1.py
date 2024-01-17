
B = len(A)
kết_quả = []
for i in A:
    if i <= B:
        kết_quả.append(i)

print(kết_quả)


# n=int(input('n='))
# for i in range (0,n):
#     a=input('')
# def build_b(a):
#     n = len(a)   
#     b = []
#     for i in range(n//2):
#         b.append(a[i] + a[n-1-i])
#     return b
# # Example usage
# b = build_b(a)
# print(b)

# def generate_permutations(elements, length, prefix=[]):
#     if length == 0:
#         print(prefix)
#         return
    
#     for element in elements:
#         new_prefix = prefix + [element]
#         generate_permutations(elements, length - 1, new_prefix)

# elements = [0, 1, 2]
# length = 4

# generate_permutations(elements, length)

def dayB(a):
    n=len(a)
    B=[]
    for i in range (n//2):
        B.append(a[i]+a[n-1-i])
    return B    
    for j in B: print(j,end=' ')