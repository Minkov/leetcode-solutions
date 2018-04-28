class Solution:
    def customSortString(self, S, T):
        chars = list(T)
        chars.sort(key=lambda x: S.find(x[0]))
        return ''.join(chars)

sol = Solution()
print(sol.customSortString("cba", "abcd"))

        
