class Solution:
    def findDuplicate(self, nums):
        n = len(nums) - 1
        total_sum = (1 + n) * n / 2.0
        for num in nums:
            total_sum -= num
        return -int(total_sum)

sol = Solution()

print(sol.findDuplicate([1, 4, 2, 5, 3, 4]))
