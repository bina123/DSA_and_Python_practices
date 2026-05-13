def contain_duplicates(nums):
    num_frequancy = set()
    
    for num in nums:
        if num in num_frequancy:
            return True
        
        num_frequancy.add(num)
        
    return False

nums = [1,1,1,3,3,4,3,2,4,2]
result = contain_duplicates(nums)
print(result)