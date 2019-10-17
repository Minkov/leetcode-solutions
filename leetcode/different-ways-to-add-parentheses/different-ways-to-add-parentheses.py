class Solution:
    def perform_operation(self, x, y, operator):
        if operator == '-':
            return x - y
        elif operator == '+':
            return x + y
        else:
            return x * y
    def calc(self, current, values, operators):
        current = values[0]
        results = []
        for i in range(len(operators)):
            val = values[i+1]
            operator = operators[i]
            results += self.calc(current, values[i+1:], operators[i+1])
            current = self.perform_operation(current, val, operator)

    def diffWaysToCompute(self, input: str):
        values = []
        operators = []
        current = 0;
        for x in input:
            if x == ' ':
                continue
            elif x in ['-', '+', '*']:
                operators.append(x)
                values.append(current)
                current = 0
            else:
                current *= 10
                current += int(x)
        values.append(current)

        return self.calc(values, operators)
sol = Solution()
