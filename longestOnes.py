def longestOnes(nums, k):
    left = 0
    zeroCount = 0
    max_length = 0
    
    for right in range(nums):
        if nums[right] == 0:
            zeroCount += 1
            
        while zeroCount > k:
            if nums[left] == 0:
                zeroCount -= 1
            left += 1
            
        max_length = max(max_length, right-left+1)