# String Manipulation & Stack - Day 6

## Overview

String manipulation and stack data structures are fundamental to many programming problems. Stacks follow the Last-In-First-Out (LIFO) principle and are perfect for matching, validation, and backtracking problems. String problems often involve pattern matching, transformation, and character-level operations.

## Problems Solved

1. **LC 20**: Valid Parentheses (Stack pattern)
2. **LC 14**: Longest Common Prefix
3. **LC 49**: Group Anagrams (String + HashMap combo)

## Stack Fundamentals

### What is a Stack?

A stack is a linear data structure that follows **LIFO (Last-In-First-Out)** principle:
- Like a stack of plates: you add to the top, remove from the top
- The last element added is the first one removed

### Stack Operations

```python
# Python uses list as stack
stack = []

# Push - add element to top
stack.append('a')
stack.append('b')
stack.append('c')
# stack = ['a', 'b', 'c']
#                    ↑ top

# Pop - remove and return top element
top = stack.pop()  # returns 'c'
# stack = ['a', 'b']
#              ↑ top

# Peek - view top without removing
if stack:
    top = stack[-1]  # 'b'

# Check if empty
if not stack:
    print("Stack is empty")

# Get size
size = len(stack)  # 2

# Clear stack
stack.clear()
```

### Time Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Push | O(1) | O(1) |
| Pop | O(1) | O(1) |
| Peek | O(1) | O(1) |
| Search | O(n) | O(1) |

## String Operations in Python

### Essential String Methods

```python
s = "Hello World"

# Case conversion
s.lower()              # "hello world"
s.upper()              # "HELLO WORLD"
s.title()              # "Hello World"
s.capitalize()         # "Hello world"

# Whitespace handling
s.strip()              # Remove leading/trailing whitespace
s.lstrip()             # Remove leading whitespace
s.rstrip()             # Remove trailing whitespace

# Splitting and joining
s.split()              # ['Hello', 'World']
s.split('o')           # ['Hell', ' W', 'rld']
'-'.join(['a','b','c']) # 'a-b-c'

# Searching
s.startswith('Hello')  # True
s.endswith('World')    # True
s.find('o')            # 4 (first occurrence)
s.index('o')           # 4 (raises error if not found)
s.count('o')           # 2

# Replacement
s.replace('World', 'Python')  # "Hello Python"

# Character checks
s.isalpha()            # False (has space)
s.isdigit()            # False
s.isalnum()            # False
s.isspace()            # False
```

### String Slicing

```python
s = "Hello World"

s[0]        # 'H' - first character
s[-1]       # 'd' - last character
s[0:5]      # 'Hello' - substring
s[:5]       # 'Hello' - from start
s[6:]       # 'World' - to end
s[::2]      # 'HloWrd' - every 2nd char
s[::-1]     # 'dlroW olleH' - reverse
```

### Character Operations

```python
# Character checks
c = 'a'
c.isalpha()            # True
c.isdigit()            # False
c.isalnum()            # True
c.islower()            # True
c.isupper()            # False

# ASCII values
ord('a')               # 97
ord('A')               # 65
chr(97)                # 'a'

# Common patterns
c.isalnum()            # Alphanumeric (a-z, A-Z, 0-9)
```

## When to Use Stack

### Key Indicators:

- ✓ Matching pairs (parentheses, brackets, quotes)
- ✓ Nested structures (HTML tags, function calls)
- ✓ Reverse order processing
- ✓ Backtracking problems
- ✓ Expression evaluation
- ✓ Undo/Redo functionality

### Keywords to Watch:

- "valid parentheses"
- "balanced brackets"
- "matching pairs"
- "nested"
- "most recent"
- "last seen"

## LC 20: Valid Parentheses (Easy) ⭐

### Problem

Given a string containing just `'(', ')', '{', '}', '[', ']'`, determine if the input string is valid.

**Valid means:**
- Open brackets must be closed by the same type
- Open brackets must be closed in the correct order

### Examples

```python
"()" → True
"()[]{}" → True
"(]" → False
"([)]" → False
"{[]}" → True
"" → True
```

### Approach: Stack + HashMap

**Key Insight:** 
- Push opening brackets onto stack
- For closing brackets, check if top of stack matches
- At end, stack should be empty

### Solution

```python
def isValid(s):
    """
    Time: O(n) - single pass through string
    Space: O(n) - stack can contain n/2 elements worst case
    """
    # Stack to store opening brackets
    stack = []
    
    # Map closing brackets to opening brackets
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    for char in s:
        if char in pairs:  # Closing bracket
            # Check if stack is empty or top doesn't match
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()  # Valid pair, remove opening bracket
        else:  # Opening bracket
            stack.append(char)
    
    # Valid only if all brackets are matched (stack empty)
    return len(stack) == 0
```

### Step-by-Step Walkthrough

```python
Input: "{[]}"

Step 1: char = '{'
  Opening bracket
  stack = ['{']

Step 2: char = '['
  Opening bracket
  stack = ['{', '[']

Step 3: char = ']'
  Closing bracket
  pairs[']'] = '['
  stack[-1] = '[' ✓ Match!
  Pop '['
  stack = ['{']

Step 4: char = '}'
  Closing bracket
  pairs['}'] = '{'
  stack[-1] = '{' ✓ Match!
  Pop '{'
  stack = []

Stack is empty → Return True ✓
```

### Why This Works

**Valid case:**
```
Input: "([])"
  '(' → stack = ['(']
  '[' → stack = ['(', '[']
  ']' → matches '[', stack = ['(']
  ')' → matches '(', stack = []
  Result: True ✓
```

**Invalid case:**
```
Input: "([)]"
  '(' → stack = ['(']
  '[' → stack = ['(', '[']
  ')' → wants '(' but top is '['
  Result: False ✗
```

### Common Mistakes

```python
# ❌ Wrong: Not checking if stack is empty
if stack[-1] != pairs[char]:  # IndexError if stack empty!
    return False

# ✅ Right: Check both conditions
if not stack or stack[-1] != pairs[char]:
    return False

# ❌ Wrong: Forgetting to check stack at end
return True  # Stack might still have unmatched brackets

# ✅ Right: Stack must be empty
return len(stack) == 0
```

### Test Cases

```python
assert isValid("()") == True
assert isValid("()[]{}") == True
assert isValid("(]") == False
assert isValid("([)]") == False
assert isValid("{[]}") == True
assert isValid("") == True
assert isValid("(") == False
assert isValid(")") == False
```

## LC 14: Longest Common Prefix (Easy)

### Problem

Find the longest common prefix string amongst an array of strings. If there is no common prefix, return `""`.

### Examples

```python
["flower","flow","flight"] → "fl"
["dog","racecar","car"] → ""
["a"] → "a"
["","b"] → ""
```

### Approach 1: Vertical Scanning (Shrinking Prefix)

**Key Insight:** Start with first string as prefix, shrink it until it matches all strings.

### Solution

```python
def longestCommonPrefix(strs):
    """
    Time: O(S) where S = sum of all characters in all strings
    Space: O(1)
    """
    if not strs:
        return ""
    
    # Use first string as initial prefix
    prefix = strs[0]
    
    # Compare with each string
    for i in range(1, len(strs)):
        # Shrink prefix until it matches start of current string
        while not strs[i].startswith(prefix):
            prefix = prefix[:-1]  # Remove last character
            if not prefix:
                return ""
    
    return prefix
```

### Step-by-Step Example

```python
Input: ["flower", "flow", "flight"]

Initial: prefix = "flower"

Compare with "flow":
  "flow".startswith("flower") → False
  prefix = "flowe"
  "flow".startswith("flowe") → False
  prefix = "flow"
  "flow".startswith("flow") → True ✓

Compare with "flight":
  "flight".startswith("flow") → False
  prefix = "flo"
  "flight".startswith("flo") → False
  prefix = "fl"
  "flight".startswith("fl") → True ✓

Return "fl"
```

### Approach 2: Horizontal Scanning (Character by Character)

```python
def longestCommonPrefix(strs):
    """
    Compare character at each position across all strings
    Time: O(S)
    Space: O(1)
    """
    if not strs:
        return ""
    
    # Compare characters at each position
    for i in range(len(strs[0])):
        char = strs[0][i]
        
        # Check if all strings have same char at position i
        for string in strs[1:]:
            # If string is too short or char doesn't match
            if i >= len(string) or string[i] != char:
                return strs[0][:i]
    
    # All of first string is common prefix
    return strs[0]
```

### Approach 3: Sort and Compare First/Last

**Key Insight:** After sorting, only need to compare first and last strings (most different).

```python
def longestCommonPrefix(strs):
    """
    Time: O(n log n) for sorting + O(m) for comparison
    Space: O(1)
    """
    if not strs:
        return ""
    
    # Sort strings
    strs.sort()
    
    # Compare first and last strings only
    first = strs[0]
    last = strs[-1]
    
    i = 0
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1
    
    return first[:i]
```

### Test Cases

```python
assert longestCommonPrefix(["flower","flow","flight"]) == "fl"
assert longestCommonPrefix(["dog","racecar","car"]) == ""
assert longestCommonPrefix(["a"]) == "a"
assert longestCommonPrefix([""]) == ""
assert longestCommonPrefix(["","b"]) == ""
assert longestCommonPrefix(["ab","a"]) == "a"
```

## LC 49: Group Anagrams (Medium) ⭐

### Problem

Given an array of strings, group the anagrams together. You can return the answer in any order.

**Anagram:** Words with same characters in different order.

### Examples

```python
Input: ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: [""]
Output: [[""]]

Input: ["a"]
Output: [["a"]]
```

### Approach 1: Sort as Key (Most Common)

**Key Insight:** Anagrams have the same characters when sorted.
- "eat" → sorted = "aet"
- "tea" → sorted = "aet"
- "ate" → sorted = "aet"

### Solution

```python
from collections import defaultdict

def groupAnagrams(strs):
    """
    Time: O(n * k log k) where n = number of strings, k = max string length
    Space: O(n * k)
    """
    # Map: sorted string → list of anagrams
    anagrams = defaultdict(list)
    
    for word in strs:
        # Sort word to get key
        key = ''.join(sorted(word))
        anagrams[key].append(word)
    
    return list(anagrams.values())
```

### Step-by-Step Example

```python
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]

Process "eat":
  key = ''.join(sorted("eat")) = "aet"
  anagrams = {"aet": ["eat"]}

Process "tea":
  key = ''.join(sorted("tea")) = "aet"
  anagrams = {"aet": ["eat", "tea"]}

Process "tan":
  key = ''.join(sorted("tan")) = "ant"
  anagrams = {"aet": ["eat", "tea"], "ant": ["tan"]}

Process "ate":
  key = ''.join(sorted("ate")) = "aet"
  anagrams = {"aet": ["eat", "tea", "ate"], "ant": ["tan"]}

Process "nat":
  key = ''.join(sorted("nat")) = "ant"
  anagrams = {"aet": ["eat", "tea", "ate"], "ant": ["tan", "nat"]}

Process "bat":
  key = ''.join(sorted("bat")) = "abt"
  anagrams = {
    "aet": ["eat", "tea", "ate"],
    "ant": ["tan", "nat"],
    "abt": ["bat"]
  }

Return: [["eat","tea","ate"], ["tan","nat"], ["bat"]]
```

### Approach 2: Character Count as Key (Optimal)

**Key Insight:** Count frequency of each character (a-z). Same counts = anagrams.

```python
from collections import defaultdict

def groupAnagrams(strs):
    """
    Time: O(n * k) where n = number of strings, k = max string length
    Space: O(n * k)
    """
    anagrams = defaultdict(list)
    
    for word in strs:
        # Count characters (a-z only)
        count = [0] * 26
        for char in word:
            count[ord(char) - ord('a')] += 1
        
        # Use tuple of counts as key
        key = tuple(count)
        anagrams[key].append(word)
    
    return list(anagrams.values())
```

### Why Tuple as Key?

```python
# Lists are unhashable (can't be dict keys)
count = [1, 2, 0, 0, ...]
# anagrams[count] = ...  # ❌ TypeError!

# Tuples are hashable (can be dict keys)
key = tuple(count)  # (1, 2, 0, 0, ...)
anagrams[key] = ...  # ✅ Works!
```

### Character Count Example

```python
"eat":
  e → count[4] = 1
  a → count[0] = 1
  t → count[19] = 1
  key = (1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0)

"tea":
  t → count[19] = 1
  e → count[4] = 1
  a → count[0] = 1
  key = (1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0)

Same key! → Anagrams ✓
```

### Test Cases

```python
result = groupAnagrams(["eat","tea","tan","ate","nat","bat"])
# Should contain: [["ate","eat","tea"], ["nat","tan"], ["bat"]]
# Order doesn't matter

assert groupAnagrams([""]) == [[""]]
assert groupAnagrams(["a"]) == [["a"]]

# Check that anagrams are grouped
result = groupAnagrams(["abc", "bca", "cab", "xyz", "zyx"])
assert len(result) == 2  # Two groups
```

## String Pattern Cheat Sheet

### Common String Patterns

| Pattern | Use When | Example Problems |
|---------|----------|-----------------|
| **Two Pointers** | Palindrome, reverse | Valid Palindrome, Reverse String |
| **HashMap** | Anagrams, frequency | Group Anagrams, Valid Anagram |
| **Stack** | Matching pairs, nested | Valid Parentheses, Min Stack |
| **Sliding Window** | Substring conditions | Longest Substring Without Repeating |
| **Sort as Key** | Group by property | Group Anagrams |
| **Set** | Unique characters | Longest Substring (no repeats) |

### Pattern Recognition

```
"valid parentheses" → Stack
"anagram" → Sort string OR count characters
"palindrome" → Two pointers (opposite direction)
"substring" → Sliding window
"common prefix/suffix" → Compare character by character
"frequency/count" → HashMap
```

## Common String Techniques

### 1. Remove Non-Alphanumeric Characters

```python
# Method 1: List comprehension
s = "Hello, World! 123"
clean = ''.join(c for c in s if c.isalnum())  # "HelloWorld123"

# Method 2: Filter
clean = ''.join(filter(str.isalnum, s))

# Method 3: Regex (import re)
import re
clean = re.sub(r'[^a-zA-Z0-9]', '', s)
```

### 2. Count Character Frequency

```python
from collections import Counter

s = "hello"
freq = Counter(s)  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# Manual counting
freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1
```

### 3. Check if Two Strings are Anagrams

```python
# Method 1: Sort
def isAnagram(s, t):
    return sorted(s) == sorted(t)

# Method 2: Counter
from collections import Counter
def isAnagram(s, t):
    return Counter(s) == Counter(t)

# Method 3: Manual count
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    
    for char in t:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False
    
    return True
```

### 4. Reverse String

```python
# Method 1: Slicing (easiest)
s = "hello"
reversed_s = s[::-1]  # "olleh"

# Method 2: reversed() function
reversed_s = ''.join(reversed(s))

# Method 3: Two pointers (in-place if list)
def reverseString(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
```

## Stack Applications in Real World

### 1. Function Call Stack

```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

# Call stack:
factorial(3)
  → factorial(2)
    → factorial(1)
    ← returns 1
  ← returns 2
← returns 6
```

### 2. Undo/Redo Functionality

```python
class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = []
        self.redo_stack = []
    
    def write(self, text):
        self.undo_stack.append(self.text)
        self.text += text
        self.redo_stack.clear()
    
    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.text)
            self.text = self.undo_stack.pop()
    
    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.text)
            self.text = self.redo_stack.pop()
```

### 3. Browser History

```python
class BrowserHistory:
    def __init__(self):
        self.back_stack = []
        self.forward_stack = []
        self.current = "homepage"
    
    def visit(self, url):
        self.back_stack.append(self.current)
        self.current = url
        self.forward_stack.clear()
    
    def back(self):
        if self.back_stack:
            self.forward_stack.append(self.current)
            self.current = self.back_stack.pop()
    
    def forward(self):
        if self.forward_stack:
            self.back_stack.append(self.current)
            self.current = self.forward_stack.pop()
```

## Common Mistakes

### Stack Mistakes

```python
# ❌ Wrong: Not checking if stack is empty before pop
stack.pop()  # IndexError if empty!

# ✅ Right: Check before pop
if stack:
    element = stack.pop()

# ❌ Wrong: Using stack when order doesn't matter
# Use set or dict instead for O(1) lookup

# ✅ Right: Stack only when order/LIFO matters
```

### String Mistakes

```python
# ❌ Wrong: Modifying string (strings are immutable!)
s = "hello"
s[0] = 'H'  # TypeError!

# ✅ Right: Create new string
s = 'H' + s[1:]  # "Hello"

# ❌ Wrong: Inefficient concatenation in loop
result = ""
for i in range(1000):
    result += str(i)  # Creates 1000 new strings!

# ✅ Right: Use list and join
result = []
for i in range(1000):
    result.append(str(i))
result = ''.join(result)  # One concatenation
```

## Time Complexity Summary

| Operation | Time | Notes |
|-----------|------|-------|
| Stack push/pop | O(1) | Constant time |
| String concatenation | O(n) | Creates new string |
| String slicing | O(k) | k = slice length |
| String sorting | O(n log n) | n = string length |
| String search | O(n*m) | n = text, m = pattern |
| Character counting | O(n) | Single pass |

## Learning Outcomes

- ✓ Understand stack LIFO principle
- ✓ Implement stack using Python list
- ✓ Recognize when to use stack (matching, validation)
- ✓ Master string manipulation methods
- ✓ Use sorted strings as keys for anagrams
- ✓ Combine multiple patterns (stack + hashmap)
- ✓ Solve validation and grouping problems efficiently

## Next Steps

- Practice LC 155 (Min Stack)
- Try LC 232 (Implement Queue using Stacks)
- Learn LC 22 (Generate Parentheses)
- Move to Day 7: Week 1 Review + NumPy/Pandas

---

**Date Completed**: ___________  
**Confidence**: ☐☐☐☐☐
