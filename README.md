# DSA_and_Python_practices

# Two Pointers problems:

1. Reverse an array - left and right pointer
2. Remove duplicates from sorted array -> Slow and fast pointer
3. Move Zeros - Slow and fast pointer
4. Validate is palindrom -> Left and right pointer

## When to Use Two Pointers

### Key Indicators:
1. **Sorted array** or need to process array from both ends
2. Need to find **pairs/triplets** with specific conditions
3. **Remove duplicates** or elements in-place
4. **Partition** array based on condition
5. **Merge** two sorted arrays
6. Find **subarray** with specific property
7. Optimize from O(n²) to O(n)

## Common Two Pointer Patterns

### Pattern 1: Opposite Direction (Left & Right)
**Use when:** Processing from both ends, finding pairs, palindrome checks

```python
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return [-1, -1]
```

**Problems:**
- Two Sum (sorted array)
- Container With Most Water
- Valid Palindrome
- 3Sum

### Pattern 2: Same Direction (Slow & Fast)
**Use when:** Remove duplicates, partition, in-place modification

```python
def remove_duplicates(arr):
    if not arr:
        return 0
    
    slow = 0  # Position for next unique element
    
    for fast in range(1, len(arr)):
        if arr[slow] != arr[fast]:
            slow += 1
            arr[slow] = arr[fast]
    
    return slow + 1  # New length
```

**Problems:**
- Remove Duplicates from Sorted Array
- Move Zeroes
- Remove Element
- Partition Array

### Pattern 3: Sliding Window (Variable Size)
**Use when:** Find subarray with sum/product condition

```python
def max_subarray_sum(arr, target):
    left = 0
    current_sum = 0
    min_length = float('inf')
    
    for right in range(len(arr)):
        current_sum += arr[right]
        
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= arr[left]
            left += 1
    
    return min_length if min_length != float('inf') else 0
```

**Problems:**
- Minimum Size Subarray Sum
- Longest Substring Without Repeating Characters
- Fruits Into Baskets

### Pattern 4: Merge Pattern
**Use when:** Merging two sorted arrays

```python
def merge_sorted_arrays(arr1, arr2):
    i, j = 0, 0
    result = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    # Add remaining elements
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    
    return result
```

**Problems:**
- Merge Sorted Array
- Intersection of Two Arrays
- Merge Two Sorted Lists

## Decision Tree: Which Pattern?

Is array sorted or can be sorted?
│
├─ YES → Need to find pairs/sum?
│         ├─ YES → Use Opposite Direction (left/right)
│         └─ NO → Need to remove/modify in-place?
│                 └─ YES → Use Same Direction (slow/fast)
│
└─ NO → Need subarray with condition?
            └─ YES → Use Sliding Window


## Common Mistakes

1. **Off-by-one errors**
   - Wrong: `while fast < len(arr) - 1`
   - Right: `while fast < len(arr)`

2. **Incrementing pointers incorrectly**
```python
   # Wrong
   if arr[slow] != arr[fast]:
       slow += 1
       fast += 1
       arr[slow] = arr[fast]  # Assigns wrong element!
   
   # Right
   if arr[slow] != arr[fast]:
       slow += 1
       arr[slow] = arr[fast]
   fast += 1  # Always increment fast
```

3. **Not handling edge cases**
   - Empty array
   - Single element
   - All duplicates
   - No valid answer


## Template Checklist

- [ ] Identify which pattern to use
- [ ] Initialize pointers correctly (0, len-1, or 0, 1)
- [ ] Define loop condition (left < right, fast < len, etc.)
- [ ] Update pointers inside loop correctly
- [ ] Handle remaining elements after loop
- [ ] Return correct value (length, array slice, indices)
- [ ] Test edge cases

# Hashmap problems
1. contains_duplicates
2. Two Sum
3. Valid anagram

# HashMap (Dictionary) Pattern - Quick Reference

## When to Use HashMap

### Key Indicators:
✅ Need **O(1) lookup** by key  
✅ **Count/frequency** of elements  
✅ Find **pairs/complements** (Two Sum)  
✅ **Group/categorize** items  
✅ Track **seen/visited** elements  
✅ Find **duplicates** or **unique** elements  
✅ **Anagram** problems  
✅ **Substring/subarray** with conditions  
✅ Can replace nested loops (O(n²) → O(n))  

### Keywords to Watch:
- "count", "frequency", "occurrences"
- "find pair that sums to X"
- "duplicate", "unique", "first unique"
- "anagram", "group by"
- "subarray with sum"
- "contains", "exists", "seen"

## Core Patterns

### Pattern 1: Frequency Counter
**Use when:** Count occurrences, find most/least frequent

```python
# Basic frequency count
def count_freq(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return freq

# Using Counter (easier)
from collections import Counter
freq = Counter(arr)
most_common = freq.most_common(1)[0]
```

**Problems:** Valid Anagram, First Unique Character, Majority Element

### Pattern 2: Two Sum / Complement
**Use when:** Find pairs with target sum/difference

```python
def two_sum(nums, target):
    seen = {}  # value -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return []
```

**Problems:** Two Sum, 3Sum, Subarray Sum Equals K

### Pattern 3: Grouping
**Use when:** Group items by common property

```python
from collections import defaultdict

def group_anagrams(words):
    groups = defaultdict(list)
    
    for word in words:
        key = ''.join(sorted(word))
        groups[key].append(word)
    
    return list(groups.values())
```

**Problems:** Group Anagrams, Group Shifted Strings

### Pattern 4: Sliding Window + HashMap
**Use when:** Substring/subarray with character constraints

```python
def longest_k_distinct(s, k):
    char_count = {}
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        # Add right character
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        # Shrink if too many distinct
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        
        max_len = max(max_len, right - left + 1)
    
    return max_len
```

**Problems:** Longest Substring Without Repeating, Minimum Window Substring

### Pattern 5: Seen/Visited Tracker
**Use when:** Track processed elements

```python
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# With distance constraint
def contains_nearby_duplicate(nums, k):
    seen = {}  # value -> last_index
    for i, num in enumerate(nums):
        if num in seen and i - seen[num] <= k:
            return True
        seen[num] = i
    return False
```

**Problems:** Contains Duplicate, Linked List Cycle, Happy Number

## Essential Dict Methods

```python
# Get with default
value = d.get(key, default_value)

# Set default if missing
d.setdefault(key, default_value)

# Increment counter
d[key] = d.get(key, 0) + 1

# Check existence
if key in d:

# Iterate
for key, value in d.items():

# Delete safely
value = d.pop(key, None)
```

## Common Mistakes

```python
# ❌ Wrong: KeyError if missing
count = d[key] + 1

# ✅ Right: Handle missing key
count = d.get(key, 0) + 1

# ❌ Wrong: Modify during iteration
for key in d:
    del d[key]

# ✅ Right: Use list of keys
for key in list(d.keys()):
    del d[key]

# ❌ Wrong: Unhashable key
d[[1, 2]] = value  # Lists can't be keys

# ✅ Right: Use tuple
d[(1, 2)] = value
```

## Decision Tree

Need to count something?
└─ YES → Frequency Counter
Find pairs with condition?
└─ YES → Two Sum/Complement
Group items?
└─ YES → Grouping Pattern
Substring with constraints?
└─ YES → Sliding Window + HashMap
Just tracking seen?
└─ YES → Seen Tracker (use Set)


## Time Complexity
- **Insert/Lookup/Delete:** O(1) average
- **Iteration:** O(n)
- **Space:** O(n)