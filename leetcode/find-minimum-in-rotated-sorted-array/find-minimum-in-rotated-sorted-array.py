class Solution:
    def findMin(self, nums) -> int:
        n = len(nums)
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if mid + 1 < n and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if mid > 0 and nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[mid] > nums[0]:
                l = mid + 1
            else:
                r = mid - 1
        return nums[0]

sol = Solution()

tests = [
    [[1, 2], 1],
    [[3,4,5,1,2], 1],
    [[4,5,6,7,0,1,2], 0]
]

for [input, expected] in tests:
    actual = sol.findMin(input)
    print(actual, expected, actual == expected)