def remove_duplicates(arr):
    if not arr:
        return arr
    
    slow = 0
    
    for fast in range(1, len(arr)):
        if arr[slow] != arr[fast]:
            slow += 1
            arr[slow] = arr[fast]
            
    return arr[:slow+1]
    
array = [1,2,3,3,4,4,5,6,6,7]
print(remove_duplicates(array))