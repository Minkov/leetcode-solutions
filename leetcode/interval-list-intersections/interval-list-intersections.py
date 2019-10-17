class Solution:
    def intervalIntersection(self, a, b):
        result = []
        last_b_index = 0
        for [a_start, a_end] in a:
            for i in range(last_b_index, len(b)):
                [b_start, b_end] = b[i]
                if a_end < b_start:
                    last_b_index = max(last_b_index - 1, 0)
                    break
                if a_start <= b_start <= a_end:
                    result.append([
                        b_start,
                        min(a_end, b_end),
                    ])
                elif a_start <= b_end <= a_end:
                    result.append([
                        max(b_start, a_start),
                        b_end,
                    ])
                elif b_start <= a_start <= b_end:
                    result.append([
                        a_start,
                        min(a_end, b_end),
                    ])
                elif b_start <= a_end <= b_end:
                    result.append([
                        max(b_start, a_start),
                        a_end,
                    ])
        return result


print(Solution().intervalIntersection([[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]))
print(Solution().intervalIntersection([[5, 10]], [[3, 10]]))
