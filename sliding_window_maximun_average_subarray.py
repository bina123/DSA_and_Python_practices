def maximum_avg_subarray(nums: list, k: int):
    current_window_sum = sum(nums[0:k])
    current_avg = current_window_sum / k
    
    for i in range(k,len(nums)):
        current_window_sum += nums[i] - nums[i-k]
        curr_avg = current_window_sum / k
        current_avg = max(current_avg, curr_avg)
        
    return current_avg

nums = [1,12,-5,-6,50,3]
k = 4

result = maximum_avg_subarray(nums, k)
print(result)