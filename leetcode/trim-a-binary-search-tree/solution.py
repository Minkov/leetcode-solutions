class Solution:
    def trimBST(self, node, l, r):
        if node == None:
            return None
        elif node.val < l:
            return self.trimBST(node.right, l, r)
        elif node.val > r:
            return self.trimBST(node.left, l, r)
        node.left = self.trimBST(node.left, l, r)
        node.right = self.trimBST(node.right, l, r)
        return node
     

