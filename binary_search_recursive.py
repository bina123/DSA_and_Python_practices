def binary_search_recursive(arr, left, right, target):
    if left > right:
        return -1
    
    mid = (left+right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr,left,mid-1,target)
    else:
        return binary_search_recursive(arr,mid+1,right,target)
    
    
    
arr = [1, 3, 5, 7, 9, 11, 13, 15]
result = binary_search_recursive(arr,0,len(arr)-1, 3)
print(result)

result1 = binary_search_recursive(arr,0,len(arr)-1, 13)
print(result1)


result2 = binary_search_recursive(arr,0,len(arr)-1, 12)
print(result2)