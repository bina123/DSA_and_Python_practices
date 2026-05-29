# Tree Traversal: DFS & BFS - Day 9

## Overview

Tree traversal is the process of visiting all nodes in a tree in a specific order. The two main approaches are:

- **DFS (Depth-First Search):** Go deep before going wide (recursion)
- **BFS (Breadth-First Search):** Go wide before going deep (queue)

Understanding both is essential for tree problems in interviews and real-world applications.

## Problems Solved

1. **LC 94**: Binary Tree Inorder Traversal (DFS)
2. **LC 102**: Binary Tree Level Order Traversal (BFS)
3. **LC 103**: Binary Tree Zigzag Level Order (BFS variant)

## Part 1: DFS (Depth-First Search)

### What is DFS?

**DFS = Go as deep as possible, then backtrack**

Like exploring a cave: you go all the way down one tunnel, hit a dead end, backtrack, then explore another tunnel.

**For trees:** Process one branch completely before moving to the next.

### The Three Types of DFS

DFS is **defined by when you process the node:**

#### **Type 1: INORDER (Left → Root → Right)**

```
       1
      / \
     2   3
    / \
   4   5

Inorder: [4, 2, 5, 1, 3]

Processing order:
  Visit 4 (leaf) → Process 4
  Backtrack to 2 → Process 2
  Visit 5 (leaf) → Process 5
  Backtrack to 1 → Process 1
  Visit 3 (leaf) → Process 3
```

**Code:**
```python
def inorder(root):
    """
    Time: O(n) - visit each node once
    Space: O(h) - recursion stack, h = height
    """
    if not root:
        return []
    
    left = inorder(root.left)      # LEFT
    current = [root.val]            # ROOT
    right = inorder(root.right)     # RIGHT
    
    return left + current + right
```

**Key Property:**
- For a Binary Search Tree (BST), inorder gives values in **sorted order**!

**Use Cases:**
- ✓ Getting sorted values from BST
- ✓ Validating BST
- ✓ In-place sorting with modification

---

#### **Type 2: PREORDER (Root → Left → Right)**

```
       1
      / \
     2   3
    / \
   4   5

Preorder: [1, 2, 4, 5, 3]

Processing order:
  Process 1 (root) → Visit children
  Process 2 (root of left) → Visit children
  Process 4 (leaf)
  Process 5 (leaf)
  Process 3 (leaf)
```

**Code:**
```python
def preorder(root):
    """
    Time: O(n) - visit each node once
    Space: O(h) - recursion stack
    """
    if not root:
        return []
    
    current = [root.val]            # ROOT (process first!)
    left = preorder(root.left)      # LEFT
    right = preorder(root.right)    # RIGHT
    
    return current + left + right
```

**Key Properties:**
- **First element is always the root**
- Used to reconstruct/clone trees

**Use Cases:**
- ✓ Creating a copy of the tree
- ✓ Serializing tree for storage
- ✓ Building expression trees

---

#### **Type 3: POSTORDER (Left → Right → Root)**

```
       1
      / \
     2   3
    / \
   4   5

Postorder: [4, 5, 2, 3, 1]

Processing order:
  Visit 4 (leaf) → Process 4
  Visit 5 (leaf) → Process 5
  Backtrack to 2 → Process 2
  Visit 3 (leaf) → Process 3
  Backtrack to 1 → Process 1
```

**Code:**
```python
def postorder(root):
    """
    Time: O(n) - visit each node once
    Space: O(h) - recursion stack
    """
    if not root:
        return []
    
    left = postorder(root.left)     # LEFT
    right = postorder(root.right)   # RIGHT
    current = [root.val]            # ROOT (process last!)
    
    return left + right + current
```

**Key Properties:**
- **Last element is always the root**
- Process children before parent

**Use Cases:**
- ✓ Deleting trees (delete children first, then parent)
- ✓ Postfix expression evaluation
- ✓ Finding subtree heights/sums

---

### DFS Comparison Table

| Traversal | Order | First | Last | Use Case |
|-----------|-------|-------|------|----------|
| **Inorder** | L-R-R | ? | ? | Sorted BST values |
| **Preorder** | R-L-R | Root | ? | Copy tree |
| **Postorder** | L-R-R | ? | Root | Delete tree |

**L = Left, R = Root, R = Right**

### DFS Template

```python
def dfs_template(root):
    # Base case
    if not root:
        return base_value
    
    # Process left subtree
    left_result = dfs_template(root.left)
    
    # Process right subtree
    right_result = dfs_template(root.right)
    
    # Combine results (order matters!)
    return combine(left_result, root.val, right_result)
```

---

## Part 2: BFS (Breadth-First Search)

### What is BFS?

**BFS = Explore level by level (like ripples in water)**

Instead of going deep, explore all neighbors at current depth before going deeper.

```
       1          ← Level 0
      / \
     2   3        ← Level 1
    / \
   4   5          ← Level 2

BFS order: [1, 2, 3, 4, 5]
(level by level, left to right)
```

### BFS Implementation

**Key tool: Queue (FIFO - First In, First Out)**

```python
from collections import deque

def bfs(root):
    """
    Level-order traversal using queue
    Time: O(n) - visit each node once
    Space: O(w) - width of tree (max nodes in one level)
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])  # Initialize with root
    
    while queue:
        node = queue.popleft()  # Get first node
        result.append(node.val)  # Process it
        
        # Add children to queue (will process later)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result
```

### Step-by-Step BFS Execution

```
Tree:
       1
      / \
     2   3
    / \
   4   5

Execution:

Initial: queue = [1], result = []

Step 1:
  Dequeue 1 → result = [1]
  Enqueue 2, 3 → queue = [2, 3]

Step 2:
  Dequeue 2 → result = [1, 2]
  Enqueue 4, 5 → queue = [3, 4, 5]

Step 3:
  Dequeue 3 → result = [1, 2, 3]
  No children → queue = [4, 5]

Step 4:
  Dequeue 4 → result = [1, 2, 3, 4]
  No children → queue = [5]

Step 5:
  Dequeue 5 → result = [1, 2, 3, 4, 5]
  Queue empty → Done!

Final: [1, 2, 3, 4, 5] ✓
```

---

## Part 3: Advanced BFS - Level Order with Nesting

### LC 102: Binary Tree Level Order Traversal

**Problem:** Return list of lists - each inner list is one level

```
       1
      / \
     2   3
    / \
   4   5

Output: [[1], [2, 3], [4, 5]]
         ↑    ↑        ↑
       Level Level    Level
         0    1        2
```

**Key Trick:** Process exactly one level per iteration

```python
def levelOrder(root):
    """
    Time: O(n) - visit each node once
    Space: O(w) - width of tree
    """
    if not root:
        return []
    
    queue = deque([root])
    result = []
    
    while queue:
        levelsize = len(queue)  # ← KEY: Number of nodes at current level
        current_level = []
        
        # Process exactly levelsize nodes (one full level)
        for _ in range(levelsize):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result
```

**The Magic:** `levelsize = len(queue)`

```
Before Level 1: queue = [2, 3]
  levelsize = 2 (exactly the nodes at level 1)
  Process 2 nodes, add their children
  Now queue = [4, 5] (level 2 nodes)

Before Level 2: queue = [4, 5]
  levelsize = 2 (exactly the nodes at level 2)
  Process 2 nodes, add their children (none)
  Queue becomes empty
```

---

### LC 103: Binary Tree Zigzag Level Order Traversal

**Problem:** Same as LC 102, but alternate direction per level

```
       1
      / \
     2   3
    / \
   4   5

Regular:  [[1], [2, 3], [4, 5]]

Zigzag:
  Level 0 (→):  [1]      (left to right)
  Level 1 (←):  [3, 2]   (right to left - REVERSED!)
  Level 2 (→):  [4, 5]   (left to right)

Output: [[1], [3, 2], [4, 5]]
```

**Solution:** Keep BFS normal, reverse VALUES per level

```python
def zigzagLevelOrder(root):
    """
    Time: O(n) - visit each node once
    Space: O(w) - width of tree
    """
    if not root:
        return []
    
    queue = deque([root])
    result = []
    reverse = False  # Track if we should reverse
    
    while queue:
        levelsize = len(queue)
        current_level = []
        
        for _ in range(levelsize):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Reverse values if odd level
        if reverse:
            current_level.reverse()
        
        result.append(current_level)
        reverse = not reverse  # Toggle for next level
    
    return result
```

**Key Insight:** Don't change BFS logic, just reverse the value list!

---

## DFS vs BFS Comparison

### Differences

| Aspect | DFS | BFS |
|--------|-----|-----|
| **Tool** | Recursion/Stack | Queue |
| **Memory** | O(h) - height | O(w) - width |
| **Order** | Varies (inorder/pre/post) | Level-by-level |
| **Code** | Elegant, recursive | Iterative, explicit |
| **When to use** | Finding paths, checking properties | Shortest path, level info |

### When to Use Which

**Use DFS when:**
- ✓ Need to go deep (find all paths)
- ✓ Check properties (valid BST, balanced tree)
- ✓ Order matters (inorder for sorted)
- ✓ Limited memory (narrower trees)
- ✓ Simple recursion preferred

**Use BFS when:**
- ✓ Need level information
- ✓ Finding shortest path
- ✓ Want to process level-by-level
- ✓ Tree is very deep (wide trees better)
- ✓ Need to serialize/deserialize

### Memory Comparison

```
Balanced tree (h = log n):
  DFS: O(log n) stack
  BFS: O(n) queue (worst case)

Skewed tree (h = n):
  DFS: O(n) stack
  BFS: O(1) queue (only stores 1 node per level)
```

---

## Common Mistakes

### Mistake 1: Wrong Order in DFS

```python
# ❌ Wrong: Returning too early
def inorder(root):
    if not root:
        return []
    
    left = inorder(root.left)
    current = [root.val]
    right = inorder(root.right)
    
    return right + current + left  # ← Wrong order!

# ✅ Correct: LEFT → ROOT → RIGHT
def inorder(root):
    if not root:
        return []
    
    left = inorder(root.left)
    current = [root.val]
    right = inorder(root.right)
    
    return left + current + right  # ← Correct order!
```

### Mistake 2: Returning Inside While Loop (BFS)

```python
# ❌ Wrong: Returns after first level only!
def levelOrder(root):
    queue = deque([root])
    result = []
    
    while queue:
        levelsize = len(queue)
        current_level = []
        
        for _ in range(levelsize):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
        return result  # ← BIG MISTAKE! Only one level!

# ✅ Correct: Return after loop completes
def levelOrder(root):
    queue = deque([root])
    result = []
    
    while queue:
        levelsize = len(queue)
        current_level = []
        
        for _ in range(levelsize):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result  # ← Return after while loop!
```

### Mistake 3: Not Using `levelsize = len(queue)`

```python
# ❌ Doesn't preserve levels properly
while queue:
    node = queue.popleft()
    result.append(node.val)
    # Adds children during iteration
    # Levels get mixed!

# ✅ Preserves one level per iteration
while queue:
    levelsize = len(queue)  # Fixed amount
    for _ in range(levelsize):
        node = queue.popleft()
        result.append(node.val)
        # Adds to next level
    # All added children form next level
```

### Mistake 4: Reversing in Wrong Place (Zigzag)

```python
# ❌ Wrong: Changes BFS logic
while queue:
    if reverse:
        node = queue.pop()  # ← Breaks level tracking!
    else:
        node = queue.popleft()
    # Children added in wrong order
    # Levels get messed up!

# ✅ Correct: Keep BFS normal, reverse VALUES
while queue:
    levelsize = len(queue)
    current_level = []
    
    for _ in range(levelsize):
        node = queue.popleft()  # ← Always same order
        current_level.append(node.val)
        # Add children normally
    
    if reverse:
        current_level.reverse()  # ← Reverse VALUES only!
```

---

## Time and Space Complexity

### Time Complexity

**All traversals: O(n)**
- Must visit each of n nodes exactly once
- No shortcuts

```
Visiting node takes O(1)
× n nodes
= O(n) total
```

### Space Complexity

**DFS:** O(h) where h = height
```
Recursion stack depth = height

Balanced tree: h = log n → O(log n)
Skewed tree:  h = n     → O(n)
```

**BFS:** O(w) where w = max width
```
Queue stores one level

Balanced tree: w = n/2  → O(n)
Very wide:    w = n     → O(n)
Single chain: w = 1     → O(1)
```

---

## Real-World Applications

### DFS Applications

1. **Detecting Cycles** (in graphs)
2. **Topological Sorting** (task scheduling)
3. **Checking Connectivity** (social networks)
4. **Backtracking** (solving Sudoku, N-queens)
5. **Finding Connected Components** (graph analysis)

### BFS Applications

1. **Shortest Path** (GPS navigation)
2. **Social Network Analysis** (degrees of separation)
3. **Web Crawling** (spider bots)
4. **Peer-to-Peer Networks** (BitTorrent)
5. **Level-by-Level Processing** (family trees, org charts)

---

## Testing Your Traversals

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def test_traversals():
    # Build test tree:
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    # Test DFS
    assert inorder(root) == [4, 2, 5, 1, 3]
    assert preorder(root) == [1, 2, 4, 5, 3]
    assert postorder(root) == [4, 5, 2, 3, 1]
    
    # Test BFS
    assert bfs(root) == [1, 2, 3, 4, 5]
    assert levelOrder(root) == [[1], [2, 3], [4, 5]]
    assert zigzagLevelOrder(root) == [[1], [3, 2], [4, 5]]
    
    print("✅ All tests passed!")

test_traversals()
```

---

## Quick Reference

### Choose Your Traversal

```
Need sorted values?
  → Inorder (for BST)

Reconstructing tree?
  → Preorder + Inorder

Deleting tree?
  → Postorder

Level information?
  → BFS (levelOrder)

Zigzag pattern?
  → BFS with reverse flag

Finding path?
  → DFS

Shortest path?
  → BFS
```

### Template Selection

```python
# For single-value return
def dfs(root):
    if not root:
        return base
    
    left = dfs(root.left)
    right = dfs(root.right)
    return combine(root.val, left, right)

# For list return
def dfs_list(root):
    if not root:
        return []
    
    left = dfs_list(root.left)
    current = [root.val]
    right = dfs_list(root.right)
    return left + current + right  # Order matters!

# For level-by-level
def bfs(root):
    if not root:
        return []
    
    queue = deque([root])
    result = []
    
    while queue:
        levelsize = len(queue)
        level = []
        
        for _ in range(levelsize):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result
```

---

## Key Takeaways

1. **DFS = Recursion**, **BFS = Queue**
2. **DFS order matters:** Inorder (L-R-R), Preorder (R-L-R), Postorder (L-R-R)
3. **BFS level size trick:** `levelsize = len(queue)` preserves levels
4. **No reversing BFS logic:** Just reverse the values for zigzag
5. **DFS space:** O(h) height, **BFS space:** O(w) width
6. **Always return AFTER loops complete**, never inside

---

## Learning Outcomes

- ✓ Master all three DFS types
- ✓ Understand when to use each
- ✓ Implement BFS with queue
- ✓ Handle level information correctly
- ✓ Solve variants (zigzag, etc)
- ✓ Know time and space tradeoffs
- ✓ Recognize common mistakes

---

## Next Steps

- Practice: LC 104 (max depth)
- Practice: LC 110 (balanced tree)
- Practice: LC 543 (diameter)
- Challenge: LC 297 (serialize/deserialize)

---

## Practice Problems

| Problem | Type | Difficulty |
|---------|------|------------|
| LC 94 | Inorder DFS | Easy |
| LC 102 | Level Order BFS | Medium |
| LC 103 | Zigzag BFS | Medium |
| LC 104 | Max Depth (DFS) | Easy |
| LC 110 | Balanced Tree (DFS) | Easy |
| LC 543 | Diameter (DFS) | Easy |
| LC 297 | Serialize Tree | Hard |

---

**Date Completed:** Day 9  
**Confidence Level:** ☐☐☐☐☐

**Key Takeaway:** "DFS and BFS are two sides of the same coin. Master the recursion vs. iteration mindset, and tree problems become straightforward."

---

## Resources

- **Visualization:** https://visualgo.net/en/bst
- **Leetcode Tag:** Tree problems
- **Practice:** 3-4 problems per type
- **Review:** Revisit mistakes in 1 week
