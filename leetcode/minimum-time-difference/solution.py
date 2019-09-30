class Solution:
    def to_minutes(self, time_point):
        [h, m] = map(int, time_point.split(':'))
        return h * 60 + m
    def findMinDifference(self, timePoints):
        timePoints = sorted(timePoints)
        max_minutes = 24 * 60 
        min_minutes = 24 * 60 + 1

        for i in range(1, len(timePoints)):
            x = self.to_minutes(timePoints[i-1])
            y = self.to_minutes(timePoints[i])
            min_minutes = min(min_minutes, y - x)
            min_minutes = min(min_minutes, max_minutes + x - y)
        return min_minutes

sol = Solution()

print(sol.findMinDifference(["23:59","00:00"]))

