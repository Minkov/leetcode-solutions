class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x

class Solution:
    def largestNumber(self, nums) -> str:
        nums = sorted(map(str, nums), key=LargerNumKey)
        return ''.join(nums)


print(Solution().largestNumber([10, 2]))
print(Solution().largestNumber([3,30,34,5,9]))