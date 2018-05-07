class Solution(object):
    def hasAlternatingBits(self, n):
        if n == 0:
            return True
        last_bit = n & 1
        n >>= 1
        while n > 0:
            current_bit = n & 1
            if current_bit == last_bit:
                return False
            last_bit = current_bit
            n >>= 1
        return True

sol = Solution()

print(sol.hasAlternatingBits(5))
print(sol.hasAlternatingBits(7))
print(sol.hasAlternatingBits(11))
print(sol.hasAlternatingBits(10))
