class Solution:
    def evaluate(self, s):
        print(s)
    def calculate(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            if s[i] == ')':
                self.evaluate(s[stack[-1]: i + 1])
                stack.pop()
            elif s[i] == ' ':
                continue
            else:
                stack.append(i)
        if s:
            self.evaluate(stack)


sol = Solution()
print(sol.calculate("(1+(4+5+2)-3)+(6+8)"))