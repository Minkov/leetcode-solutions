class Solution:
    def numRabbits(self, answers):
        answers = list(set(answers))
        return sum(answers) + len(answers)

sol = Solution()

print(sol.numRabbits([1, 1, 2]))
print(sol.numRabbits([10, 10, 10]))
print(sol.numRabbits([1, 1, 2, 10, 10, 10]))
print(sol.numRabbits([11, 10, 10]))
print(sol.numRabbits([]))
