# Sorting Algorithms - Day 5

## Overview

Sorting is the process of arranging data in a particular order (ascending or descending). It's fundamental to computer science and enables efficient searching, data analysis, and optimization. Understanding sorting algorithms helps you choose the right approach for different scenarios.

## Problems Solved

1. **LC 912**: Sort an Array
2. **LC 75**: Sort Colors (Dutch National Flag)
3. **LC 347**: Top K Frequent Elements

## Why Learn Sorting?

- **Foundation**: Many algorithms rely on sorted data (binary search, merge algorithms)
- **Interviews**: Common topic in technical interviews
- **Real-world**: Data preprocessing, rankings, finding top-K elements
- **AI/ML**: Feature engineering, model evaluation, data analysis

## Sorting Algorithms Comparison

| Algorithm | Best | Average | Worst | Space | Stable? | When to Use |
|-----------|------|---------|-------|-------|---------|-------------|
| **Bubble Sort** | O(n) | O(n²) | O(n²) | O(1) | Yes | Almost sorted, educational |
| **Selection Sort** | O(n²) | O(n²) | O(n²) | O(1) | No | Memory limited (few writes) |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) | Yes | Small/nearly sorted data |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | Large datasets, stable sort |
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | O(log n) | No | General purpose, in-place |
| **Heap Sort** | O(n log n) | O(n log n) | O(n log n) | O(1) | No | Guaranteed O(n log n) |
| **Python sort()** | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | **Use this in practice!** |

**Stable Sort**: Maintains relative order of equal elements

## Basic Sorting Algorithms

### 1. Bubble Sort

**Concept**: Repeatedly swap adjacent elements if they're in wrong order. Largest element "bubbles" to the end.

```python
def bubble_sort(arr):
    """
    Time: O(n²) average, O(n) best (already sorted)
    Space: O(1)
    Stable: Yes
    """
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # Optimization: stop if no swaps (already sorted)
        if not swapped:
            break
    
    return arr
```

**Visual Example**:
```
[5, 2, 8, 1, 9]
[2, 5, 1, 8, 9]  # After pass 1
[2, 1, 5, 8, 9]  # After pass 2
[1, 2, 5, 8, 9]  # After pass 3 ✓
```

**When to Use**:
- Nearly sorted data (O(n) best case)
- Educational purposes
- Small datasets where simplicity matters

### 2. Selection Sort

**Concept**: Find minimum element and put it at the beginning. Repeat for remaining unsorted portion.

```python
def selection_sort(arr):
    """
    Time: O(n²) always
    Space: O(1)
    Stable: No
    """
    n = len(arr)
    
    for i in range(n):
        # Find minimum in unsorted portion
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap minimum with first unsorted element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr
```

**Visual Example**:
```
[5, 2, 8, 1, 9]
[1, 2, 8, 5, 9]  # Found min=1, swapped with 5
[1, 2, 8, 5, 9]  # Found min=2, already in place
[1, 2, 5, 8, 9]  # Found min=5, swapped with 8
[1, 2, 5, 8, 9]  # Sorted ✓
```

**When to Use**:
- Memory is very limited (makes fewest writes)
- Small datasets
- When you need to minimize swaps

### 3. Insertion Sort

**Concept**: Build sorted array one element at a time by inserting each element into its correct position.

```python
def insertion_sort(arr):
    """
    Time: O(n²) average, O(n) best (already sorted)
    Space: O(1)
    Stable: Yes
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insert key at correct position
        arr[j + 1] = key
    
    return arr
```

**Visual Example**:
```
[5, 2, 8, 1, 9]
[2, 5, 8, 1, 9]  # Inserted 2 before 5
[2, 5, 8, 1, 9]  # 8 already in place
[1, 2, 5, 8, 9]  # Inserted 1 at beginning
[1, 2, 5, 8, 9]  # 9 already in place ✓
```

**When to Use**:
- Small datasets (< 50 elements)
- Nearly sorted data (very efficient!)
- Online algorithm (can sort as data arrives)
- Linked lists (no random access needed)

## Advanced Sorting (Good to Know)

### Merge Sort

**Concept**: Divide array in half, recursively sort both halves, then merge them.

```python
def merge_sort(arr):
    """
    Time: O(n log n) always
    Space: O(n)
    Stable: Yes
    """
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Conquer (merge)
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

**When to Use**:
- Large datasets
- Need guaranteed O(n log n)
- Need stable sort
- External sorting (data doesn't fit in memory)

### Quick Sort

**Concept**: Pick a pivot, partition array around it, recursively sort partitions.

```python
def quick_sort(arr):
    """
    Time: O(n log n) average, O(n²) worst
    Space: O(log n) for recursion
    Stable: No
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)
```

**When to Use**:
- General purpose sorting
- In-place sorting needed
- Average case performance matters

## Python's Built-in Sorting

### Use `sorted()` and `.sort()` in Real Code!

```python
# sorted() - returns new sorted list
arr = [5, 2, 8, 1, 9]
sorted_arr = sorted(arr)
print(arr)        # [5, 2, 8, 1, 9] - original unchanged
print(sorted_arr) # [1, 2, 5, 8, 9]

# .sort() - sorts in-place
arr = [5, 2, 8, 1, 9]
arr.sort()
print(arr)  # [1, 2, 5, 8, 9] - original modified

# Reverse sorting
sorted(arr, reverse=True)  # [9, 8, 5, 2, 1]

# Sort by custom key
words = ['apple', 'pie', 'a', 'cherry']
sorted(words, key=len)  # ['a', 'pie', 'apple', 'cherry']

# Sort tuples by second element
pairs = [(1, 5), (3, 2), (2, 8)]
sorted(pairs, key=lambda x: x[1])  # [(3, 2), (1, 5), (2, 8)]

# Sort dictionary by values
d = {'a': 3, 'b': 1, 'c': 2}
sorted(d.items(), key=lambda x: x[1])  # [('b', 1), ('c', 2), ('a', 3)]
```

**Why Python's sort() is best**:
- Uses **Timsort** (hybrid of merge + insertion)
- Optimized for real-world data
- Handles partially sorted data efficiently
- Stable (maintains relative order)
- Written in C (very fast)

## LeetCode Problems

### LC 912: Sort an Array

```python
def sortArray(nums):
    """
    Just use Python's built-in sort
    Time: O(n log n)
    Space: O(n)
    """
    return sorted(nums)
    # or: nums.sort(); return nums
```

### LC 75: Sort Colors (Dutch National Flag)

**Problem**: Sort array containing only 0s, 1s, and 2s in-place in one pass.

```python
def sortColors(nums):
    """
    Three-way partitioning with 3 pointers
    Time: O(n)
    Space: O(1)
    """
    low, mid, high = 0, 0, len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            # Swap with low pointer
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            # Already in correct position
            mid += 1
        else:  # nums[mid] == 2
            # Swap with high pointer
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
            # Don't increment mid (need to check swapped element)
```

**Visual Example**:
```
[2, 0, 2, 1, 1, 0]
 L  M           H

[0, 0, 2, 1, 1, 2]  # After processing
 L     M        H

[0, 0, 1, 1, 2, 2]  # Final
```

**Key Insight**: 
- `low` marks end of 0s
- `mid` is current element being examined
- `high` marks start of 2s
- Everything before `low` is 0
- Everything between `low` and `mid` is 1
- Everything after `high` is 2

### LC 347: Top K Frequent Elements

```python
from collections import Counter
import heapq

def topKFrequent(nums, k):
    """
    Method 1: Counter + sort
    Time: O(n log n)
    Space: O(n)
    """
    count = Counter(nums)
    return [num for num, freq in count.most_common(k)]

def topKFrequent_heap(nums, k):
    """
    Method 2: Counter + heap (better for large n, small k)
    Time: O(n log k)
    Space: O(n)
    """
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)

def topKFrequent_bucket(nums, k):
    """
    Method 3: Bucket sort (optimal)
    Time: O(n)
    Space: O(n)
    """
    count = Counter(nums)
    
    # Bucket: index = frequency, value = list of numbers
    buckets = [[] for _ in range(len(nums) + 1)]
    
    for num, freq in count.items():
        buckets[freq].append(num)
    
    # Collect top k from highest frequency buckets
    result = []
    for i in range(len(buckets) - 1, -1, -1):
        result.extend(buckets[i])
        if len(result) >= k:
            return result[:k]
```

## When to Use Each Sort

### Use Built-in `sorted()` When:
- ✓ General purpose sorting
- ✓ Production code
- ✓ Need stable sort
- ✓ Performance matters

### Use Custom Sort When:
- Interview explicitly asks to implement
- Learning algorithm concepts
- Specific constraints (in-place, stable, etc.)

### Algorithm Selection Guide:

```
Size < 50 elements?
└─ YES → Insertion Sort

Nearly sorted data?
└─ YES → Insertion Sort or Bubble Sort

Memory severely limited?
└─ YES → Selection Sort or Heap Sort

Need stable sort?
└─ YES → Merge Sort or Python's sort()

Need guaranteed O(n log n)?
└─ YES → Merge Sort or Heap Sort

General purpose?
└─ YES → Python's sort() or Quick Sort
```

## Sorting in AI/ML

### Data Preprocessing
```python
# Sort before binary search
data = sorted(raw_data)
index = binary_search(data, target)

# Percentile calculation
sorted_data = sorted(values)
p95 = sorted_data[int(len(sorted_data) * 0.95)]
```

### Feature Engineering
```python
# Rank features
feature_importance = sorted(features, key=lambda x: x.score, reverse=True)

# Binning/discretization
sorted_vals = sorted(continuous_feature)
bins = [sorted_vals[i*100] for i in range(10)]
```

### Model Evaluation
```python
# Sort predictions by confidence
predictions = sorted(results, key=lambda x: x.confidence, reverse=True)

# Top-K accuracy
top_k = sorted(predictions, reverse=True)[:k]
```

## Time Complexity Intuition

**O(n²) Algorithms** (Bubble, Selection, Insertion):
- Two nested loops
- Compare every element with every other element
- Fine for small data (< 100 elements)

**O(n log n) Algorithms** (Merge, Quick, Heap):
- Divide and conquer or tree-based
- Much faster for large data
- Standard for general sorting

**Visual Comparison**:
```
n = 100:    O(n²) = 10,000 ops    O(n log n) = 664 ops
n = 1,000:  O(n²) = 1,000,000     O(n log n) = 9,966
n = 10,000: O(n²) = 100,000,000   O(n log n) = 132,877

For n=10,000: O(n log n) is ~750x faster!
```

## Common Mistakes

### 1. Not using built-in sort in real code
```python
# ❌ Don't implement your own in production
def my_sort(arr):
    # ... bubble sort ...

# ✅ Use Python's optimized sort
arr.sort()
```

### 2. Forgetting sort is in-place vs returns new list
```python
# ❌ Wrong
arr = [3, 1, 2]
arr.sort()
print(sorted(arr))  # [1, 2, 3] but arr was already sorted by .sort()

# ✅ Right
arr = [3, 1, 2]
sorted_arr = sorted(arr)  # New list
# or
arr.sort()  # In-place
```

### 3. Modifying list while iterating
```python
# ❌ Wrong
for i in range(len(arr)):
    arr.sort()  # Don't sort inside loop!

# ✅ Right
arr.sort()  # Sort once before loop
for i in range(len(arr)):
    # process sorted array
```

## Testing Your Sorts

```python
def test_sorting():
    test_cases = [
        [5, 2, 8, 1, 9],           # Random
        [1, 2, 3, 4, 5],           # Already sorted
        [5, 4, 3, 2, 1],           # Reverse sorted
        [3, 3, 3, 3],              # All same
        [1],                        # Single element
        [],                         # Empty
        [2, 1],                     # Two elements
    ]
    
    for arr in test_cases:
        original = arr.copy()
        result = bubble_sort(arr.copy())
        expected = sorted(original)
        
        assert result == expected, f"Failed on {original}"
    
    print("✅ All tests passed!")

test_sorting()
```

## Learning Outcomes

- ✓ Understand O(n²) vs O(n log n) trade-offs
- ✓ Know when to use each algorithm
- ✓ Implement basic sorts from scratch
- ✓ Use Python's built-in sort efficiently
- ✓ Apply sorting to real problems

## Next Steps

- Practice LC 912, 75, 347
- Learn merge sort and quick sort (Day 6)
- Understand heap sort
- Study counting sort and radix sort (for integers)
- Move to Day 6: String manipulation

---

**Date Completed**: ___________  
**Confidence**: ☐☐☐☐☐
