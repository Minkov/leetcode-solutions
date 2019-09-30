class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        rows_count = len(grid)
        cols_count = len(grid[0])
        rows = []
        cols = []
        for row in range(rows_count):
            best_cell = max(grid[row])
            rows.append(best_cell)
        for col in range(cols_count):
            best_cell = -1
            for row in range(rows_count):
                best_cell = max(best_cell, grid[row][col])
            cols.append(best_cell)

        count = 0
        for row in range(rows_count):
            for col in range(cols_count):
                count += grid[row][col] - min(rows[row], cols[col])
        return -count


sol = Solution()

print(sol.maxIncreaseKeepingSkyline(
    [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]))
