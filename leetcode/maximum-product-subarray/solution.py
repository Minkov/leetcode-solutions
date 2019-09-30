class Solution:
    def maxProduct(self, nums):
        left = [nums[0]]
        for i in range(1, len(nums)):
            left.append(nums[i] * left[-1])
        right = [nums[-1]]
        for i in range(len(nums) - 2, -1, -1):
            right.append(nums[i] * right[-1])
        right = right[::-1]
        max_prod = nums[0]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                left_prod = 1
                if i > 0:
                    left_prod = left[i - 1]
                    if left_prod == 0:
                        left_prod = 1

                right_prod = 1
                if j < len(right) - 1:
                    right_prod = right[j + 1]
                    if right_prod == 0:
                        right_prod = 1

                prod = left[-1] / (left_prod * right_prod)
                max_prod = max(max_prod, prod)
        max_num = max(nums)
        max_prod = max(max_num, int(max_prod))
        max_prod = max(max_prod, max(left))
        max_prod = max(max_prod, max(right))
        return max_prod

sol = Solution()

print(sol.maxProduct([2,3,-2,4]))
print(sol.maxProduct([-2,0,-1]))
print(sol.maxProduct([-3,0,1,-2]))
print(sol.maxProduct([-1,-2,-3,0]))
