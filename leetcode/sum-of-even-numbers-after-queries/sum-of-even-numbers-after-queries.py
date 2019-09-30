class Solution:
    def sumEvenAfterQueries(self, A, queries):
        results = [sum(filter(lambda x: x % 2 == 0, A))]
        for [value, index] in queries:
            old_value = A[index]
            A[index] += value
            if A[index] % 2 == 0:
                if value % 2 == 0:
                    results.append(results[-1] + value)
                else:
                    results.append(results[-1] + A[index])
            else:
                if value % 2 == 0:
                    results.append(results[-1])
                else:
                    results.append(results[-1] - old_value)
        return results[1:]

print(Solution().sumEvenAfterQueries([1,2,3,4], [[1,0],[-3,1],[-4,0],[2,3]]))

