def reverse_array(arr):
    l,r = 0, len(arr) - 1
    
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        
        l += 1
        r -= 1
        
    return arr
    
    
array = [1,2,3,4,5,6,7,8]
print(reverse_array(array))