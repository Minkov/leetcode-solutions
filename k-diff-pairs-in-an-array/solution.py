class Solution:
    def binary_search(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return -1
    def count_repeating(self, nums):
        used = set()
        repeating = set()
        for num in nums:
            if num in used:
                repeating.add(num)
            used.add(num)

        return len(repeating)
        
    def findPairs(self, nums, k):
        if k < 0:
            return 0
        if k is 0:
            return self.count_repeating(nums)

        nums = list(sorted(set(nums)))
        count = 0

        for num in nums:
            if num - k < 0:
                continue
            index = self.binary_search(nums, num - k)
            if index >= 0:
                count += 1
        return count
sol = Solution()

print(sol.findPairs([3, 1, 4, 1, 5], 2))
print(sol.findPairs([1, 2, 3, 4, 5], 1))
print(sol.findPairs([1, 2, 3, 4, 5], 2))
print(sol.findPairs([1, 3, 1, 5, 4], 0))
print(sol.findPairs([1, 2, 3, 4, 5], -1))
