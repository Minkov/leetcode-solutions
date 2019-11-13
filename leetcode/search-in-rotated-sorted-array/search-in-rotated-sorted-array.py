class Solution:
    def search(self, nums, target: int) -> int:
        n = len(nums)
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                l = mid + 1
            else:
                r = mid - 1
        return -1


sol = Solution()

tests = [
    [[[4, 5, 6, 7, 0, 1, 2], 0], 4],
    [[[4, 5, 6, 7, 0, 1, 2], 3], -1],
]

for [input, expected] in tests:
    [arr, searched] = input
    actual = sol.search(arr, searched)
    print(actual, expected, actual == expected)
