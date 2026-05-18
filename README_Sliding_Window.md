# Sliding Window Pattern - Day 3

## Overview

Sliding window is an optimization technique for problems involving subarrays or substrings. It reduces time complexity from O(n²) or O(n³) to O(n) by maintaining a window that slides through the array.

## Problems Solved

1. **LC 121**: Best Time to Buy and Sell Stock
2. **LC 3**: Longest Substring Without Repeating Characters
3. **LC 643**: Maximum Average Subarray I
4. **LC 1004**: Max Consecutive Ones III (bonus)

## When to Use Sliding Window

**Key Indicators:**
- ✓ Find subarray/substring with specific property
- ✓ Maximum/minimum in subarrays
- ✓ Longest/shortest subarray meeting condition
- ✓ Contains contiguous elements (no gaps)
- ✓ Time series or sequence analysis

## Type 1: Fixed-Size Window

**Use when:** Window size k is given

```python
def max_sum_subarray(arr, k):
    # Calculate sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window
    for i in range(k, len(arr)):
        # Add new element, remove old element
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

**Time**: O(n), **Space**: O(1)

## Type 2: Variable-Size Window

**Use when:** Finding longest/shortest subarray with condition

```python
def longest_substring_k_distinct(s, k):
    char_count = {}
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        # Expand: Add right character
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        # Contract: Shrink if invalid
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        
        # Update result
        max_len = max(max_len, right - left + 1)
    
    return max_len
```

## Template Code

```python
# Variable Window Template
def sliding_window_variable(arr):
    left = 0
    result = 0
    # window state (sum, count, set, etc.)
    
    for right in range(len(arr)):
        # 1. Add arr[right] to window
        # Update window state
        
        # 2. While window is invalid:
        while condition_not_met:
            # Remove arr[left] from window
            # Update window state
            left += 1
        
        # 3. Update result
        result = max(result, right - left + 1)
    
    return result
```

## Key Insights

1. **Two pointers**: left and right (both start at 0)
2. **Right pointer** always moves forward (expand)
3. **Left pointer** moves when window becomes invalid (contract)
4. **Each element** visited at most twice (once by right, once by left)
5. **Window size** = right - left + 1

## Example Problems

### LC 121: Best Time to Buy and Sell Stock

```python
def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    
    return max_profit
```

### LC 3: Longest Substring Without Repeating

```python
def lengthOfLongestSubstring(s):
    char_set = set()
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    
    return max_len
```

### LC 1004: Max Consecutive Ones III

```python
def longestOnes(nums, k):
    left = 0
    zeros_count = 0
    max_length = 0
    
    for right in range(len(nums)):
        if nums[right] == 0:
            zeros_count += 1
        
        while zeros_count > k:
            if nums[left] == 0:
                zeros_count -= 1
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length
```

## Common Mistakes

### 1. Forgetting to update window state when shrinking

```python
# Always remove arr[left] from state before incrementing left
while condition_not_met:
    # Update state first
    char_count[s[left]] -= 1
    left += 1  # Then move pointer
```

### 2. Using wrong loop condition

```python
# Use 'while' for shrinking (not 'if')
# Might need multiple shrinks
while window_invalid:
    shrink()
```

### 3. Updating result at wrong time

```python
# Update result AFTER shrinking, when window is valid
for right in range(len(arr)):
    add_to_window(arr[right])
    
    while window_invalid:
        shrink_from_left()
    
    # Now window is valid, update result
    result = max(result, window_size)
```

## Visual Example

Finding max sum subarray of size 3 in [2, 1, 5, 1, 3, 2]:

```
Step 1: [2, 1, 5] -> sum = 8
Step 2: [1, 5, 1] -> sum = 7 (remove 2, add 1)
Step 3: [5, 1, 3] -> sum = 9 (remove 1, add 3) ← maximum
Step 4: [1, 3, 2] -> sum = 6 (remove 5, add 2)
```

## Time and Space Complexity

- **Time**: O(n) - each element visited at most twice
- **Space**: O(1) for fixed window, O(k) for variable (k = unique elements in window)

## Learning Outcomes

- ✓ Optimize subarray problems from O(n²) to O(n)
- ✓ Distinguish fixed vs variable window
- ✓ Maintain window state efficiently
- ✓ Apply to time series and sequence problems

## Next Steps

- Practice LC 424 (Longest Repeating Character Replacement)
- Try LC 209 (Minimum Size Subarray Sum)
- Move to Day 4: Binary Search

---

**Date Completed**: ___________  
**Confidence**: ☐☐☐☐☐
