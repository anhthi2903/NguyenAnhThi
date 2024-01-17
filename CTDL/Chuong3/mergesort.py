def mergeSort(A):
    if len(A) > 1:
        mid = len(A) // 2
        left = A[:mid]
        right = A[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # The value from the left half has been used
              A[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                A[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            A[k]=right[j]
            j += 1
            k += 1

A = [29,10,13,14,37]
mergeSort(A)
print(A)