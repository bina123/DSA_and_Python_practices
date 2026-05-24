# Binary Trees - Day 8

## Overview

A binary tree is a hierarchical data structure where each node has at most two children (left and right). Trees are fundamental in computer science and appear in file systems, databases, decision-making algorithms, and many other applications.

## Problems Solved

1. **LC 104**: Maximum Depth of Binary Tree
2. **LC 226**: Invert Binary Tree
3. **LC 100**: Same Tree

## Tree Fundamentals

### What is a Binary Tree?

**Definition:** A tree where each node has:
- A value
- At most 2 children (left and right)
- One parent (except root)

**Example:**
```
       1          ← Root
      / \
     2   3        ← Level 1
    / \
   4   5          ← Level 2 (Leaves)
```

### Tree Terminology

| Term | Definition | Example |
|------|------------|---------|
| **Root** | Top node with no parent | Node 1 |
| **Leaf** | Node with no children | Nodes 3, 4, 5 |
| **Parent** | Node with children | Node 2 is parent of 4 and 5 |
| **Child** | Node below another | Nodes 2 and 3 are children of 1 |
| **Siblings** | Nodes with same parent | Nodes 2 and 3 |
| **Height** | Longest path from node to leaf | Tree above has height 2 |
| **Depth** | Distance from root to node | Node 4 has depth 2 |
| **Level** | All nodes at same depth | Level 1 has nodes 2 and 3 |

### TreeNode Structure

**In Python:**
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

**Creating a tree:**
```python
# Build this tree:
#     1
#    / \
#   2   3

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
```

## The Recursion Pattern

**99% of tree problems use recursion!**

### Core Template

```python
def tree_function(root):
    # Base case: empty tree
    if not root:
        return base_value
    
    # Recursive case: process subtrees
    left_result = tree_function(root.left)
    right_result = tree_function(root.right)
    
    # Combine results
    return combine(root.val, left_result, right_result)
```

### Why Recursion Works for Trees

**Trees are recursive by nature:**
- A tree is a root + left subtree + right subtree
- Each subtree is also a tree!
- Process each subtree the same way

**Example: Count nodes**
```
       1
      / \
     2   3
    / \
   4   5

count(1) = 1 + count(2) + count(3)
count(2) = 1 + count(4) + count(5)
count(4) = 1 + count(None) + count(None) = 1
count(5) = 1
count(3) = 1
Total = 5 ✓
```

## Practice Functions

### 1. Count Nodes

```python
def count_nodes(root):
    """Count total nodes in tree"""
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)
```

**Time:** O(n) - visit each node once  
**Space:** O(h) - recursion stack, h = height

### 2. Sum Tree

```python
def sum_tree(root):
    """Sum all values in tree"""
    if not root:
        return 0
    return root.val + sum_tree(root.left) + sum_tree(root.right)
```

### 3. Find Maximum Value

```python
def max_value(root):
    """Find maximum value in tree"""
    if not root:
        return float('-inf')
    return max(root.val, max_value(root.left), max_value(root.right))
```

**Why `-inf` for empty tree?**
- If all values are negative, we still get correct max
- Example: tree with [-5, -3, -10] → max = -3

## LeetCode Problems

### LC 104: Maximum Depth of Binary Tree (Easy)

**Problem:** Find the maximum depth (height) of a binary tree.

**Example:**
```
    3
   / \
  9  20
    /  \
   15   7

Output: 3
```

**Solution:**
```python
def maxDepth(root):
    """
    Time: O(n) - visit every node
    Space: O(h) - recursion stack
    """
    if not root:
        return 0
    
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
```

**How it works:**
```
maxDepth(3):
  left = maxDepth(9) = 1 + max(0, 0) = 1
  right = maxDepth(20):
           left = maxDepth(15) = 1
           right = maxDepth(7) = 1
           = 1 + max(1, 1) = 2
  = 1 + max(1, 2) = 3 ✓
```

**Key insight:** Depth = 1 (current level) + max of left and right depths

---

### LC 226: Invert Binary Tree (Easy)

**Problem:** Invert a binary tree (mirror it left-right).

**Example:**
```
Input:         Output:
    4              4
   / \            / \
  2   7          7   2
 / \ / \        / \ / \
1  3 6  9      9  6 3  1
```

**Solution:**
```python
def invertTree(root):
    """
    Time: O(n) - visit every node
    Space: O(h) - recursion stack
    """
    if not root:
        return None
    
    # Swap left and right children
    root.left, root.right = root.right, root.left
    
    # Recursively invert both subtrees
    invertTree(root.left)
    invertTree(root.right)
    
    return root
```

**Visual walkthrough:**
```
Original:      After swap     After recurse
    4              4               4
   / \            / \             / \
  2   7          7   2           7   2
 / \ / \        / \ / \         / \ / \
1  3 6  9      9  6 3  1       9  6 3  1

Step 1: Swap 2 and 7 at root
Step 2: Recurse on 7 (was left, now right) - swap 9 and 6
Step 3: Recurse on 2 (was right, now left) - swap 1 and 3
```

**Key insight:** Swap children, then recursively invert both subtrees

**Common mistake:**
```python
# ❌ Don't check if children exist!
if root.left and root.right:
    root.left, root.right = root.right, root.left

# ✅ Just swap (works even if one or both are None)
root.left, root.right = root.right, root.left
```

---

### LC 100: Same Tree (Easy)

**Problem:** Check if two binary trees are identical.

**Example:**
```
Tree p:    Tree q:
   1          1
  / \        / \
 2   3      2   3

Output: True
```

**Solution:**
```python
def isSameTree(p, q):
    """
    Time: O(min(n, m)) - check until difference found
    Space: O(min(h_p, h_q)) - recursion stack
    """
    # Both empty - same
    if not p and not q:
        return True
    
    # One empty, one not - different
    if not p or not q:
        return False
    
    # Values don't match - different
    if p.val != q.val:
        return False
    
    # Check both subtrees recursively
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
```

**Decision tree:**
```
Both None? → True
One None? → False
Values different? → False
Otherwise → Check left AND right subtrees
```

**One-liner version:**
```python
def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
```

---

## Common Tree Patterns

### Pattern 1: Process Current Node

**Use when:** Need to check/modify current node

```python
def pattern1(root):
    if not root:
        return base_value
    
    # Process current node
    result = do_something(root.val)
    
    # Recurse
    left = pattern1(root.left)
    right = pattern1(root.right)
    
    return combine(result, left, right)
```

**Examples:** Count nodes, sum values, find max

### Pattern 2: Check Property

**Use when:** Validating tree property

```python
def pattern2(root):
    if not root:
        return True
    
    # Check current node
    if not valid(root):
        return False
    
    # Both subtrees must satisfy property
    return pattern2(root.left) and pattern2(root.right)
```

**Examples:** Same tree, valid BST, balanced tree

### Pattern 3: Divide and Conquer

**Use when:** Combine results from subtrees

```python
def pattern3(root):
    if not root:
        return base_value
    
    # Get results from subtrees
    left_result = pattern3(root.left)
    right_result = pattern3(root.right)
    
    # Combine with current node
    return combine(root.val, left_result, right_result)
```

**Examples:** Max depth, diameter, path sum

## Time and Space Complexity

### Time Complexity

**Most tree recursion: O(n)**
- Must visit each node once
- n = number of nodes

**Exceptions:**
- Balanced tree specific operations: O(log n)
- Finding element in BST: O(h) where h = height

### Space Complexity

**Recursion stack: O(h)**
- h = height of tree
- Best case (balanced): h = log n
- Worst case (skewed): h = n

**Example:**
```
Balanced tree:      Skewed tree:
     1                  1
    / \                  \
   2   3                  2
  / \                      \
 4   5                      3
                             \
Height = 2                    4
Stack = O(log n)         Height = 3
                         Stack = O(n)
```

## Common Mistakes

### 1. Forgetting Base Case

```python
# ❌ Wrong: Stack overflow!
def count_nodes(root):
    return 1 + count_nodes(root.left) + count_nodes(root.right)

# ✅ Right: Handle empty tree
def count_nodes(root):
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)
```

### 2. Checking Children Before Recursion

```python
# ❌ Wrong: Unnecessary checks
if root.left:
    invertTree(root.left)
if root.right:
    invertTree(root.right)

# ✅ Right: Base case handles None
invertTree(root.left)
invertTree(root.right)
```

**The base case `if not root: return None` is your safety net!**

### 3. Wrong Attribute Names

```python
# ❌ Wrong: TreeNode uses .val, .left, .right
root.value
root.data

# ✅ Right: 
root.val
root.left
root.right
```

### 4. Trying to Be Too Clever

```python
# ❌ Complicated: Calculating height to get node count
def count_nodes(root):
    height = maxDepth(root)
    return 2**height - 1  # Only works for perfect trees!

# ✅ Simple: Just count directly
def count_nodes(root):
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)
```

## Types of Binary Trees

### 1. Full Binary Tree
Every node has 0 or 2 children (no node has only 1 child)

```
     1
    / \
   2   3
  / \
 4   5
```

### 2. Complete Binary Tree
All levels filled except possibly last, which is filled left-to-right

```
     1
    / \
   2   3
  / \  /
 4  5 6
```

### 3. Perfect Binary Tree
All internal nodes have 2 children, all leaves at same level

```
     1
    / \
   2   3
  / \ / \
 4  5 6  7
```

### 4. Balanced Binary Tree
Height of left and right subtrees differ by at most 1

```
     1
    / \
   2   3
  /
 4
Height difference = 1 ✓
```

### 5. Binary Search Tree (BST)
Left subtree < root < right subtree

```
     4
    / \
   2   6
  / \ / \
 1  3 5  7
```

## When to Use Trees

**Use binary trees when:**
- ✓ Hierarchical data (file systems, org charts)
- ✓ Fast search with BST (O(log n))
- ✓ Expression parsing (math expressions)
- ✓ Decision making (decision trees in ML)
- ✓ Efficient insertion/deletion with ordering

**Don't use when:**
- ❌ Need frequent random access (use arrays)
- ❌ Simple linear data (use lists)
- ❌ Need FIFO/LIFO only (use queue/stack)

## Trees in AI/ML

### 1. Decision Trees
```
   Age < 30?
   /       \
 Yes       No
  |         |
Buy    Don't Buy
```

### 2. Random Forests
Ensemble of decision trees for classification/regression

### 3. Expression Trees
```
      +
     / \
    *   3
   / \
  2   4

Represents: (2 * 4) + 3
```

### 4. Hierarchical Clustering
Tree structure showing data similarity

## Testing Your Trees

```python
def test_tree_functions():
    # Build test tree:
    #     5
    #    / \
    #   3   8
    #  / \
    # 1   4
    
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(4)
    
    # Test count
    assert count_nodes(root) == 5
    
    # Test sum
    assert sum_tree(root) == 21  # 5+3+8+1+4
    
    # Test max
    assert max_value(root) == 8
    
    # Test depth
    assert maxDepth(root) == 3
    
    print("✅ All tests passed!")

test_tree_functions()
```

## Quick Reference

### Recursion Checklist

When solving tree problems:

- [ ] Write base case first (`if not root`)
- [ ] Decide what to return for empty tree
- [ ] Recurse on left subtree
- [ ] Recurse on right subtree
- [ ] Combine results
- [ ] Don't check if children exist before recursing

### Time/Space Quick Guide

| Operation | Time | Space |
|-----------|------|-------|
| Traverse all nodes | O(n) | O(h) |
| Find max/min | O(n) | O(h) |
| Count nodes | O(n) | O(h) |
| Check property | O(n) | O(h) |
| BST search | O(h) | O(h) |

h = height (log n for balanced, n for skewed)

## Learning Outcomes

- ✓ Understand binary tree structure
- ✓ Master tree recursion pattern
- ✓ Solve tree problems with confidence
- ✓ Know when to use different base cases
- ✓ Recognize common tree patterns
- ✓ Avoid common mistakes

## Next Steps

- Day 9: Tree Traversal (DFS - Inorder, Preorder, Postorder)
- Day 10: BFS (Level Order Traversal)
- Practice: LC 543 (Diameter of Binary Tree)
- Practice: LC 110 (Balanced Binary Tree)

## Resources

- **Video**: NeetCode Tree Playlist
- **Visualizer**: https://visualgo.net/en/bst
- **Practice**: LeetCode Tree Tag

---

**Date Completed**: ___________  
**Confidence**: ☐☐☐☐☐

**Key Takeaway**: "Trees are recursive by nature. Master the base case, and the rest follows naturally."
