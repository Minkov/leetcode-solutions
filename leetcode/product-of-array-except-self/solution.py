class Solution:
    def productExceptSelf(self, nums):
        if len(nums) == 1:
            return [1]

        before = [0] * len(nums)
        before[0] = 1
        for i in range(1, len(nums)):
            before[i] = before[i - 1] * nums[i - 1]

        after = [0] * len(nums)
        after[-1] = 1
        for i in range(len(nums) - 2, -1, -1):
            after[i] = after[i + 1] * nums[i + 1]

        result = []
        for i in range(len(nums)):
            result.append(before[i] * after[i])
        return result


sol = Solution()

print(sol.productExceptSelf([1, 2, 3, 4]))
print(sol.productExceptSelf([1, -1]))
