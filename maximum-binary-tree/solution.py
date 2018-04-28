

class Solution(object):
    def find_index_of_max(self, nums, from_index, to_index):
        best_index = from_index
        best_value = nums[best_index]
        for i in range(from_index, to_index):
            if nums[i] > best_value:
                best_value = nums[i]
                best_index = i
        return best_index

    def build_subtree(self, nums, from_index, to_index):
        if from_index >= to_index:
          return None

        index = self.find_index_of_max(nums, from_index, to_index)
        node = TreeNode(nums[index])
        node.left = self.build_subtree(nums, from_index, index)
        node.right = self.build_subtree(nums, index + 1, to_index)
        return node
    
    def constructMaximumBinaryTree(self, nums):
        return self.build_subtree(nums, 0, len(nums))
        


