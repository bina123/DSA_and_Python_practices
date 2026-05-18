def binary_search(arr, k):
    n = len(arr);
    
    left = 0
    right = n-1
    while left <= right:
        mid = (left+right) // 2
        
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            right = mid - 1
        else:
            left = mid + 1
            
    return -1

arr = [1, 3, 5, 7, 9, 11, 13, 15]
result = binary_search(arr, 3)
print(result)

result1 = binary_search(arr, 13)
print(result1)


result2 = binary_search(arr, 12)
print(result2)
