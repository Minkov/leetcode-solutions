class Solution:
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals = sorted(intervals)

        result = [intervals[0]]
        if not intervals:
            return intervals

        for interval in intervals:
            if interval[0] <= result[-1][1]:
                result[-1][1] = max(
                    result[-1][1],
                interval[1])
            else:
                result.append(interval)
        return result


tests = [
    [[[1,5],[10,11],[15,2147483647]], [5,7]],
    [[], [2,5 ]],
    [[[1, 5]], [0, 1]],
    [[[1, 2]], [2, 5]],
    [[[1, 2]], [3, 5]],
    [[[1,3],[6,9]], [2,5 ]],
    [[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4,8]]
]

for [intervals, new_interval] in tests:
    print('-' * 10)
    print(intervals)
    print(new_interval)
    print(Solution().insert(intervals, new_interval))