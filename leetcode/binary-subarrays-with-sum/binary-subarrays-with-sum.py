class Solution:
    def numSubarraysWithSum(self, A, S):
        if not A:
            return 0
        result = 0
        current = sum(A)
        if current == S:
            result += 1
        result += self.numSubarraysWithSum(A[0:len(A) - 1], S)
        result += self.numSubarraysWithSum(A[1:], S)
        return result


print(Solution().numSubarraysWithSum([1, 0, 1, 0, 1, 0], 2))
print(Solution().numSubarraysWithSum([1, 0, 1, 0, 1], 2))
print(Solution().numSubarraysWithSum([0, 0, 0, 0, 0], 0))
