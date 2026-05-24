class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def count_nodes(root):
    if not root:
        return 0
    
    return 1 + count_nodes(root.left)+ count_nodes(root.right)
    


def sum_tree(root):
    if not root:
        return 0
        
    return root.val + sum_tree(root.left) + sum_tree(root.right)
    
def max_value(root):
    if not root:
        return float("-inf")
    
    return max(root.val, max_value(root.left), max_value(root.right))

# Test
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)

print(f"Count: {count_nodes(root)}")   # 5
print(f"Sum: {sum_tree(root)}")        # 21
print(f"Max: {max_value(root)}")       # 8