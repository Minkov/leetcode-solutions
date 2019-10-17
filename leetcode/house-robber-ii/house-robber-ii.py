class Solution:
    def rob(self, nums) -> int:
        n = len(nums)

        i = len(nums) - 3
        result = [nums[0]]

        for i in range(1, n-1):

            i -= 1
        return result

print(Solution().rob([2,3,2]))
print(Solution().rob([1,2,3,1]))