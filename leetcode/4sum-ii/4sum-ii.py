class Solution:
    def fourSumCount(self, a, b, c, d):
        result = 0
        sums = {}
        for x in a:
            for y in b:
                sums[x+y] = sums.get(x + y, 0) + 1
        for x in c:
            for y in d:
                result += sums.get(-(x + y), 0)

        return result

print(Solution().fourSumCount(
    [1, 2],
    [-2, -1],
    [-1, 2],
    [0, 2])
)

print(Solution().fourSumCount(
    [0, 1, -1],
    [-1, 1, 0],
    [0, 0, 1],
    [-1, 1, 1]
))
