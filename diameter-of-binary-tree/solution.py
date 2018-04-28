class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def print_me(self, indent=''):
        if self.left is not None:
            self.left.print_me(indent + '--')
        print('%s %d' % (indent, self.val))
        if self.right is not None:
            self.right.print_me(indent + '--')


class Solution:
    def calc_depth(self, root):
        if root is None:
            return 0
        left_depth = 1 + \
            self.calc_depth(root.left) if root.left is not None else 1
        right_depth = 1 + \
            self.calc_depth(root.right) if root.right is not None else 1

        return max(left_depth, right_depth)

    def diameterOfBinaryTree(self, root):
        if root is None:
            return 0

        left_depth = self.calc_depth(root.left)
        right_depth = self.calc_depth(root.right)
        left_subtree = self.diameterOfBinaryTree(root.left)
        right_subtree = self.diameterOfBinaryTree(root.right)

        best_len = max(left_depth + right_depth, left_subtree, right_subtree)
        return best_len


def build_tree(values, index=0):
    if index >= len(values):
        return None
    if values[index] is None:
        return None

    root = TreeNode(values[index])
    root.left = build_tree(values, index * 2 + 1)
    root.right = build_tree(values, index * 2 + 2)
    return root


sol = Solution()

# print(sol.diameterOfBinaryTree(build_tree([1, 2, 3, 4, 5])))

root2 = build_tree([1, 2, None, 4, 5, None, None, 1, None, 7, None])
root2.print_me()
print(sol.diameterOfBinaryTree(root2))
