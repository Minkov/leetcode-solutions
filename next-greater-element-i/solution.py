class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        stack = []
        result_dict = dict()
        for num in nums:
            while len(stack) > 0 and stack[-1] < num:
                result_dict[stack[-1]] = num
                stack.pop()
            stack.append(num)
        result = [result_dict[num] if num in result_dict else -1 for num in findNums]
        return result
        
sol = Solution()

print(sol.nextGreaterElement([2,4], [1,2,3,4]))
print(sol.nextGreaterElement([4,1,2], [1,3,4,2]))

