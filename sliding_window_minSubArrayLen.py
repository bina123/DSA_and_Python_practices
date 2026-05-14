def minSubArrayLen(target: int, nums: list):
    left = 0
    right = 0
    sumOfCurrentWindow = 0
    result = float('inf')
    
    for right in range(len(nums)):
        sumOfCurrentWindow += nums[right]
        
        while sumOfCurrentWindow >= target:
            result = min(result, right - left + 1)
            sumOfCurrentWindow -= nums[left]
            left += 1
            
    return result if result != float('inf') else 0

target = 7
nums = [2,3,1,2,4,3]
result = minSubArrayLen(target, nums)
print(result)

target1 = 4
nums1 = [1,4,4]
result1 = minSubArrayLen(target1, nums1)
print(result1)