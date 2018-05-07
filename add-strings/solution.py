class Solution:
    def addStrings(self, num1, num2):
        num1 = list(map(int, num1))
        num2 = list(map(int, num2))
        if len(num1) < len(num2):
            [num1, num2] = [num2, num1]

        remainder = 0
        index = 1
        while index <= len(num2):
            num1[-index] += num2[-index] + remainder
            remainder = num1[-index] // 10
            num1[-index] %= 10
            index += 1
        
        index = -len(num2) - 1
        
        while remainder > 0 and -index <= len(num1):
            num1[index] += remainder
            remainder = num1[index] // 10
            num1[index] %= 10
            index -= 1
        if remainder > 0:
            num1.insert(0, 1)
        return ''.join(map(str, num1))
            
        
sol = Solution()

print(sol.addStrings("9", "99"))
