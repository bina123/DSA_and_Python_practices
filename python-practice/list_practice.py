def squares_of_evens(num):
    return [x**2 for x in range(num+1) if x%2 == 0]

def flatten_nested_list(arr):
    return [item for sublist in arr for item in sublist]

def filter_and_transform(numbers, threshold):
    """Keep numbers > threshold and square them"""
    return [x**2 for x in numbers if x > threshold]

def swap_pairs(arr):
    result = []
    
    for i in range(0,len(arr) - 1,2):
        a,b = arr[i],arr[i+1]
        result.extend([b,a])
    if len(arr) % 2 == 1:
        result.append(arr[-1])
        
    return result

def invert_dict(d):
    """Swap keys and values"""
    return {v: k for k, v in d.items()}

def merge_dicts(d1, d2):
    """Merge two dictionaries"""
    result = d1.copy()
    result.update(d2)
    return result
    # or in Python 3.9+: return d1 | d2
    
print(squares_of_evens(10))  # [0, 4, 16, 36, 64, 100]
print(flatten_nested_list([[1,2], [3,4], [5]]))  # [1,2,3,4,5]
print(swap_pairs([1,2,3,4,5]))  # [2,1,4,3,5]