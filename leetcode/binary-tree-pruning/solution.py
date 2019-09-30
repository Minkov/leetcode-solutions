class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pruneTree(self, root):
        if root is None:
            return None

        left_result = self.pruneTree(root.left)
        right_result = self.pruneTree(root.right)

        if left_result is None:
            root.left = None
        if right_result is None:
            root.right = None
        if root.val is 0 and root.left == None and root.right == None:
            return None
        return root


sol = Solution()


