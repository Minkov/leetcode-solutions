class Solution:
    def is_self_dividing(self, num):
        digits = map(int, str(num))

        for digit in digits:
            if digit is 0:
                return False
            if num % digit is not 0:
                return False
        return True
    def selfDividingNumbers(self, left, right):
        result = [num for num in range(left, right + 1) if self.is_self_dividing(num)]
        return result
            
        
        



sol = Solution()

print(sol.selfDividingNumbers(1, 22))

