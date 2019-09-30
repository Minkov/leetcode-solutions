class Solution:
    def numberOfArithmeticSlices(self, A):
        if len(A) < 3:
            return 0
        a = A
        d = self.make_sequences(a)
        counts_per_length = self.calc_counts_per_length(max(d))
        result = 0
        for i in range(0, len(d)):
            if i == len(d) - 1 and d[i] >= 3:
                result += counts_per_length[d[i]]
            if i < len(d) - 1 and d[i] >= 3 and d[i] > d[i + 1]:
                result += counts_per_length[d[i]]
        return result

    def calc_counts_per_length(self, l):
        d = [-1, -1, -1, 1]
        for i in range(4, l + 3):
            d.append(d[i - 1] + i - 3 + 1)
        return d

    def make_sequences(self, a):
        d = [0] * len(a)
        d[0] = 1
        d[1] = 2
        for i in range(2, len(a)):
            if a[i - 2] - a[i - 1] == a[i - 1] - a[i]:
                d[i] = d[i - 1] + 1
            else:
                d[i] = 2
        return d


sol = Solution()

print(sol.numberOfArithmeticSlices([1, 2, 3, 4]))
print(sol.numberOfArithmeticSlices([1, 2, 3, 4, 5]))
print(sol.numberOfArithmeticSlices([1, 2, 3, 4, 5, 6]))
print(sol.numberOfArithmeticSlices([1, 2, 3, 4, 6, 8, 10, 7, 7, 7, 7, 7]))
