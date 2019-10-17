class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        vals = [5**i for i in range(1, 16)]
        for i in range(5, n + 1, 5):
            x = i
            for j in range(len(vals) - 1, -1, -1):
                val = vals[j]
                while x % val == 0:
                    result += j + 1
                    x //= val
        return result


sol = Solution()
print(sol.trailingZeroes(3))
print(sol.trailingZeroes(5))
print(sol.trailingZeroes(10))
print(sol.trailingZeroes(1808548329))