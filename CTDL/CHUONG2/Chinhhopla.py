# s = []
# k=int(input('k='))
# n=int(input('n='))
# i=1
# j=1
# check = False
# def display(s):
#     for q in range (0, len(s)):
#         print(s[q], end="")
#         s = []
# def Try(i,j):
#     if (i<n and j<k):
#         s.append(i)
#         j+=1
#     if (j==k):
#         j=1
#         i+=1
#         display(s)
    
# Try(1,1)
def combination_with_repetition(arr, r):
    result = []
    def generate_combinations(combination, index):
        if len(combination) == r:
            result.append(combination)
            return
        for i in range(index, len(arr)):
            generate_combinations(combination + [arr[i]], i)
        
    generate_combinations([], 0)
    return result

# Ví dụ sử dụng
arr = [1, 2, 3]
r = 2
combinations = combination_with_repetition(arr, r)
print(combinations)
