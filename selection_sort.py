def selection_sort(nums):
    n = len(nums)
    
    for i in range(n-1):
        minIdx = i
        for j in range(i+1,n):
            if nums[j] < nums[minIdx]:
                minIdx = j
        
        nums[i], nums[minIdx] = nums[minIdx], nums[i]
        
    return nums
    
nums = [64, 34, 25, 12, 22, 11, 90]
result = selection_sort(nums)
print(result)
