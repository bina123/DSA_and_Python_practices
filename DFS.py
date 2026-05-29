class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Write these from scratch:

def inorder(root):
    """Return list in inorder: LEFT → ROOT → RIGHT"""
    if not root:
        return []
    
    left = inorder(root.left)
    current = [root.val]
    right = inorder(root.right)
    return left + current + right

def preorder(root):
    """Return list in preorder: ROOT → LEFT → RIGHT"""
    if not root:
        return []
    
    current = [root.val]
    left = preorder(root.left)
    right = preorder(root.right)
    return current + left + right

def postorder(root):
    """Return list in postorder: LEFT → RIGHT → ROOT"""
    if not root:
        return []
    
    left = postorder(root.left)
    right = postorder(root.right)
    current = [root.val]
    
    return left + right + current

# Test with this tree:
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

print(f"Inorder: {inorder(root)}")      # Should be [4, 2, 5, 1, 3]
print(f"Preorder: {preorder(root)}")    # Should be [1, 2, 4, 5, 3]
print(f"Postorder: {postorder(root)}")  # Should be [4, 5, 2, 3, 1]