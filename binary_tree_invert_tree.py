# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    if not root:
        return None
    
    root.left, root.right = root.right, root.left
        
    invertTree(root.left)
    invertTree(root.right)
    
    return root

# Test Case 1: Both children
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

inverted = invertTree(root)
print(inverted)
# Should be: 4 → (7,2) → (9,6,3,1)

# Test Case 2: Only left child
root2 = TreeNode(1)
root2.left = TreeNode(2)

inverted2 = invertTree(root2)
print(inverted2)
# Should be: 1 → (None, 2)

# Test Case 3: Empty
inverted3 = invertTree(None)
print(inverted3)
# Should be: None