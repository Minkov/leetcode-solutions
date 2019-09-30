class Solution:
    def sortedSquares(self, A):
        return sorted(map(lambda x: x * x, A))


print(Solution().sortedSquares([-4,-1,0,3,10]))

print(Solution().sortedSquares([-7,-3,2,3,11]))