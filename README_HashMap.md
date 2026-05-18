# HashMap (Dictionary) Pattern - Day 2

## Overview

A HashMap (or dictionary in Python) provides O(1) average time for insert, lookup, and delete operations. It's essential for optimizing algorithms from O(n²) to O(n).

## Problems Solved

1. **LC 217**: Contains Duplicate
2. **LC 1**: Two Sum
3. **LC 242**: Valid Anagram

## When to Use HashMap

**Key Indicators:**
- ✓ Need O(1) lookup by key
- ✓ Count/frequency of elements
- ✓ Find pairs/complements (Two Sum)
- ✓ Group/categorize items
- ✓ Track seen/visited elements
- ✓ Find duplicates or unique elements
- ✓ Anagram problems
- ✓ Replace nested loops (O(n²) → O(n))

**Keywords to Watch:**
- "count", "frequency", "occurrences"
- "find pair that sums to X"
- "duplicate", "unique", "first unique"
- "anagram", "group by"
- "contains", "exists", "seen"

## Pattern 1: Frequency Counter

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

**Use for:** Valid Anagram, First Unique Character, Majority Element

## Pattern 2: Two Sum / Complement

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

**Use for:** Two Sum, 3Sum, Subarray Sum Equals K

## Pattern 3: Grouping

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

**Use for:** Group Anagrams, Group Shifted Strings

## Pattern 4: Seen/Visited Tracker

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

**Use for:** Contains Duplicate, Linked List Cycle, Happy Number

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

### 1. KeyError when accessing missing key

```python
# ❌ Wrong: KeyError if missing
count = d[key] + 1

# ✅ Right: Handle missing key
count = d.get(key, 0) + 1
```

### 2. Modifying dict during iteration

```python
# ❌ Wrong: Modify during iteration
for key in d:
    del d[key]

# ✅ Right: Use list of keys
for key in list(d.keys()):
    del d[key]
```

### 3. Using unhashable types as keys

```python
# ❌ Wrong: Lists can't be keys
d[[1, 2]] = value

# ✅ Right: Use tuple
d[(1, 2)] = value
```

## Decision Tree

```
Need to count something?
└─ YES → Frequency Counter

Find pairs with condition?
└─ YES → Two Sum/Complement

Group items?
└─ YES → Grouping Pattern

Just tracking seen?
└─ YES → Seen Tracker (use Set)
```

## Time Complexity

- **Insert/Lookup/Delete**: O(1) average
- **Iteration**: O(n)
- **Space**: O(n)

## Learning Outcomes

- ✓ Use HashMap for O(1) lookups
- ✓ Optimize brute force O(n²) to O(n)
- ✓ Track frequency, seen elements, complements
- ✓ Handle dictionary operations safely

## Next Steps

- Practice LC 49 (Group Anagrams)
- Try LC 387 (First Unique Character)
- Move to Day 3: Sliding Window

---

**Date Completed**: ___________  
**Confidence**: ☐☐☐☐☐
