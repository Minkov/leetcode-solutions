class Solution:
    def mergeTrees(self, root1, root2):
        if root1 == None and root2 == None:
            return None
        if root1 != None and root2 == None:
            return root1
        if root1 == None and root2 != None:
            return root2

        node = TreeNode(root1.val + root2.val)
        node.left = self.mergeTrees(root1.left, root2.left)
        node.right = self.mergeTrees(root1.right, root2.right)
        return node


