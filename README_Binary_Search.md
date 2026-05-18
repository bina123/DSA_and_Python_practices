# Binary Search Pattern - Day 4

## Overview

Binary search is a divide-and-conquer algorithm that works on sorted arrays. It achieves O(log n) time complexity by repeatedly halving the search space.

## Problems Solved

1. **LC 704**: Binary Search
2. **LC 35**: Search Insert Position
3. **LC 278**: First Bad Version

## Core Implementation

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half
    
    return -1  # Not found
```

## When to Use Binary Search

**Key Indicators:**
- ✓ Array is sorted (or can be sorted)
- ✓ Need O(log n) search time
- ✓ Random access is available (arrays, not linked lists)
- ✓ Searching for value, boundary, or condition

## Pattern 1: Find Exact Match

```python
while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
return -1
```

**Use for**: LC 704 (Binary Search)

## Pattern 2: Find Insert Position

```python
while left <= right:
    mid = (left + right) // 2
    if arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
return left  # Insert position
```

**Key insight**: When loop ends, `left` is the insert position

**Use for**: LC 35 (Search Insert Position)

## Pattern 3: Find Boundary (First/Last Occurrence)

```python
while left < right:  # No equals
    mid = (left + right) // 2
    if condition:
        right = mid  # Don't exclude mid
    else:
        left = mid + 1
return left
```

**Use for**: LC 278 (First Bad Version)

## Example Problems

### LC 704: Binary Search

```python
def search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
```

### LC 35: Search Insert Position

```python
def searchInsert(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left
```

### LC 278: First Bad Version

```python
def firstBadVersion(n):
    left, right = 1, n
    
    while left < right:
        mid = (left + right) // 2
        
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    
    return left
```

## Visual Example

Searching for 7 in [1, 3, 5, 7, 9, 11, 13, 15]:

```
Step 1: [1, 3, 5, 7, 9, 11, 13, 15]
         L           M            R
         Compare: 9 > 7, search left

Step 2: [1, 3, 5, 7]
         L     M   R
         Compare: 5 < 7, search right

Step 3:       [7]
               L
               M
               R
         Found! Return index 3
```

## Time and Space Complexity

- **Time**: O(log n) - halves search space each iteration
- **Space**: O(1) for iterative, O(log n) for recursive

## Why O(log n)?

Each step eliminates half the elements:

```
Array size: n → n/2 → n/4 → n/8 → ... → 1
Number of steps = log₂(n)

Example: Array of 1,000,000 elements = ~20 steps
```

## Common Mistakes

### 1. Using wrong loop condition

```python
# Use left <= right for exact match
while left <= right:

# Use left < right for boundary
while left < right:
```

### 2. Infinite loop when finding boundary

```python
# ❌ Wrong: Can cause infinite loop
left = mid

# ✅ Right: Always progresses
left = mid + 1
```

### 3. Not handling empty array

```python
# Always check if array is empty
if not arr:
    return -1
```

### 4. Integer overflow (not in Python, but good practice)

```python
# Instead of
mid = (left + right) // 2

# Can use (safer in C++/Java)
mid = left + (right - left) // 2
```

## Recursive Implementation (Bonus)

```python
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Usage
result = binary_search_recursive(arr, target, 0, len(arr) - 1)
```

## Real-World Applications

- Finding optimal hyperparameters (learning rate)
- Threshold selection for classification
- Searching in large sorted datasets
- Database indexing
- Game development (collision detection)

## Testing Your Implementation

```python
def test_binary_search():
    arr = [1, 3, 5, 7, 9]
    
    assert binary_search(arr, 5) == 2  # Middle
    assert binary_search(arr, 1) == 0  # Start
    assert binary_search(arr, 9) == 4  # End
    assert binary_search(arr, 6) == -1  # Not found
    assert binary_search([], 5) == -1  # Empty
    assert binary_search([5], 5) == 0  # Single element
    assert binary_search([5], 3) == -1  # Single, not found
    
    print("✅ All tests passed!")
```

## Performance Comparison

```python
import time

# Linear search vs Binary search on 1,000,000 elements
arr = list(range(1000000))
target = 999999

# Linear: ~0.045 seconds
# Binary: ~0.000002 seconds
# Binary is 22,500x faster!
```

## Learning Outcomes

- ✓ Understand O(log n) complexity
- ✓ Recognize three main patterns
- ✓ Avoid infinite loops and off-by-one errors
- ✓ Apply to sorted array problems
- ✓ Know when to use <= vs <

## Next Steps

- Practice LC 33 (Search in Rotated Sorted Array)
- Try LC 153 (Find Minimum in Rotated Sorted Array)
- Move to Day 5: Sorting Algorithms

---

**Date Completed**: ___________  
**Confidence**: ☐☐☐☐☐
