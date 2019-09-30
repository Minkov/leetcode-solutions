class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def check_validity(self, root, min_node, max_node):
        if root is None:
            return True
        if min_node < root.val < max_node:
            left_result = self.check_validity(root.left, min_node, root.val)
            right_result = self.check_validity(root.right, root.val, max_node)
            return left_result and right_result
        return False

    def isValidBST(self, root):
        return self.check_validity(root, - 1 << 20, 1 << 20)


root = TreeNode(1)
root.left = TreeNode(1)

print(Solution().isValidBST(root))
print('-' * 10)

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
print(Solution().isValidBST(root2))
