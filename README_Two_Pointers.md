# Two Pointers Pattern - Day 1-2

## Overview

Two pointers is an optimization technique that uses two references (pointers) to traverse data structures, typically arrays. It reduces time complexity from O(n²) to O(n) for many problems.

## Problems Solved

1. **LC 26**: Remove Duplicates from Sorted Array
2. **LC 283**: Move Zeroes
3. **LC 125**: Valid Palindrome

## Pattern 1: Opposite Direction (Left & Right)

**Use when:**
- Processing array from both ends
- Finding pairs with target sum
- Palindrome validation
- Container with most water problems

**Example: Valid Palindrome**

```python
def is_palindrome(s):
    # Convert to lowercase and keep only alphanumeric
    s = ''.join(c.lower() for c in s if c.isalnum())
    
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True
```

## Pattern 2: Same Direction (Slow & Fast)

**Use when:**
- Remove duplicates in-place
- Partition array by condition
- Move elements (like zeros) to end

**Example: Remove Duplicates**

```python
def remove_duplicates(nums):
    if not nums:
        return 0
    
    slow = 0  # Position for next unique element
    
    for fast in range(1, len(nums)):
        if nums[slow] != nums[fast]:
            slow += 1
            nums[slow] = nums[fast]
    
    return slow + 1  # New length
```

**Example: Move Zeroes**

```python
def move_zeroes(nums):
    slow = 0  # Position for next non-zero
    
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
```

## When to Use Two Pointers

**Key Indicators:**
- ✓ Sorted array or can process from both ends
- ✓ Find pairs/triplets with specific conditions
- ✓ Remove duplicates or elements in-place
- ✓ Partition array based on condition
- ✓ Optimize from O(n²) to O(n)

## Common Mistakes

### 1. Off-by-one errors in loop conditions
```python
# Wrong
while fast < len(arr) - 1:

# Right
while fast < len(arr):
```

### 2. Incrementing pointers incorrectly
Always increment fast pointer; only increment slow when condition met.

### 3. Not handling edge cases
- Empty array
- Single element
- All duplicates

## Time and Space Complexity

- **Time**: O(n) - single pass through array
- **Space**: O(1) - only using two pointers

## Template Code

```python
# Opposite Direction Template
def opposite_direction(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        # Process arr[left] and arr[right]
        # Move pointers based on condition
        left += 1
        right -= 1

# Same Direction Template
def same_direction(arr):
    slow = 0
    
    for fast in range(len(arr)):
        if condition:
            # Process arr[fast]
            arr[slow] = arr[fast]
            slow += 1
    
    return slow
```

## Learning Outcomes

- ✓ Understand two pointer optimization
- ✓ Recognize when to use opposite vs same direction
- ✓ Solve problems in O(n) instead of O(n²)
- ✓ Handle in-place array modifications

## Next Steps

- Practice LC 11 (Container With Most Water)
- Try LC 15 (3Sum) for triplet problems
- Move to Day 3: Sliding Window pattern

---

**Date Completed**: ___________  
**Confidence**: ☐☐☐☐☐
