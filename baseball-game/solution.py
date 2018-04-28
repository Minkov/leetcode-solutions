class Solution:
    def calPoints(self, ops):
        points = []
        result = 0
        for op in ops:
            if op == 'C':
                update = points.pop()
                result -= update
            else:
                update = 0
                if op == 'D':
                    update = points[-1] * 2
                elif op == '+':
                    update = points[-1] + points[-2]
                else:
                    update = int(op)
 
                points.append(update)
                result += update

        return result


sol = Solution()

print(sol.calPoints(["5","2","C","D","+"]))
print(sol.calPoints(["5","-2","4","C","D","9","+","+"]))
