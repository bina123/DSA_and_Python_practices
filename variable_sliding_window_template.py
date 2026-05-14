def variable_window(arr):
    left = 0
    result = 0
    char_set = set()
    
    for right in range(arr):
        while arr[right] in char_set:
            char_set.remove(arr[left])
            left += 1
        
        char_set.add(arr[right])
        result = max(result, right-left+1)
        
    return result