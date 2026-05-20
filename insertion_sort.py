def insertion_sort(nums):
    n = len(nums);
    
    for i in range(1,n):
        key= nums[i]
        j = i-1
        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
        
    return nums 

nums = [64, 34, 25, 12, 22, 11, 90]
result = insertion_sort(nums)
print(result)