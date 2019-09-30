class Solution:
    def decide(self, n):
        if n % 15 == 0:
            return "FizzBuzz"
        elif n % 5 == 0:
            return "Buzz"
        elif n % 3 == 0:
             return "Fizz"
        return str(n)
    def fizzBuzz(self, n):
        result = [self.decide(x) for x in range(1, n + 1)]
        return result

sol = Solution()

print(sol.fizzBuzz(15))

