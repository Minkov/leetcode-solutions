class Solution:
    def countSmaller(self, nums):
        sorted = []
        result = []

        for num in nums[::-1]:
            index = self.find_index(sorted, num)
            sorted.insert(index, num)
            result.append(index)
        return result[::-1]

    def find_index(self, nums, num):
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= num:
                right = mid 
            else:
                left = mid + 1
        return right
sol = Solution()

print(sol.countSmaller([5]))
print(sol.countSmaller([5, 1]))
print(sol.countSmaller([5, 5]))
print(sol.countSmaller([5, 6]))
print(sol.countSmaller([5, 2, 6, 1]))

print(sol.countSmaller([5, 2, 6, 1, 3, 2, 1]))
