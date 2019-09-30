class Solution:
    def permute(self, index, n, used):
        # import pdb; pdb.set_trace()
        if index is n + 1:
            return 1
        
        result = 0
        for i in range(1, n + 1):
            if i in used:
                continue
            if index % i != 0 and i % index != 0:
                continue

            used.add(i)
            r = self.permute(index + 1, n, used)
            result += r
            used.remove(i)
        return result  

    def countArrangement(self, n):
        used = set()
        result = 0
        for i in range(1, n + 1):
            used.add(i)
            result += self.permute(2, n, used)
            used.remove(i)
        return result

sol = Solution()
print(sol.countArrangement(2))
