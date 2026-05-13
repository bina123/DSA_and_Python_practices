from collections import defaultdict

def two_sum(nums, target):
    if not nums:
        return
    
    result_hash = defaultdict()
    
    for index, num in enumerate(nums):
        complement = target - num
        if complement in result_hash:
            return [result_hash[complement],index]
        
        result_hash[num] = index

nums = [2,7,11,15]
target = 22
print(two_sum(nums, target))