class Solution:
    def findComplement(self, num):
        if num is 0:
            return 1

        bin_num = []
        while num > 0:
            bin_num.append(num & 1)
            num >>= 1
        bin_num = bin_num[::-1]
        
        bin_result = [0 if b is 1 else 1 for b in bin_num]

        result = 0
        for b in bin_result:
            result <<= 1
            result |= b

        return result
        
sol = Solution()

print(sol.findComplement(0))
print(sol.findComplement(1))
print(sol.findComplement(5))
print(sol.findComplement(2))

"""
2 -> 10
     01
"""
