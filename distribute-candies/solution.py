class Solution:
    def distributeCandies(self, candies):
        kinds = set(candies)
        return min(len(candies) // 2, len(kinds))


sol = Solution()

print(sol.distributeCandies([1, 1, 2, 2, 3, 3]))
print(sol.distributeCandies([1, 1, 2, 3]))
