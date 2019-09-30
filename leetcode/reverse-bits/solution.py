class Solution:
    def to_binary(self, num):
        result = []
        while num > 0:
            result.append(num & 1)
            num >>= 1
        result += [0] * (32 - len(result))
        return result[::-1]
    def to_dec(self, bits):
        num = 0
        for b in bits:
            num <<= 1
            num |= b
        return num
    def reverseBits(self, n):
        bin_n = self.to_binary(n)
        bin_result = bin_n[::-1]
        result = self.to_dec(bin_result)
        return result


sol = Solution()

print(43261596)
print(sol.reverseBits(43261596))

