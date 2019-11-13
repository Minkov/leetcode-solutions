class Solution:
    def maximumGap(self, nums) -> int:
        if not nums or len(nums) < 2:
            return 0
        nums.sort()
        print(nums)
        curr = -1
        for i in range(1, len(nums)):
            curr = max(curr, nums[i] - nums[i-1])
        return curr


print(Solution().maximumGap([3,6,9,1]))

