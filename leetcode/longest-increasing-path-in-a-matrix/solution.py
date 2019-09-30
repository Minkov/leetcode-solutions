class Solution:
    def in_range(self, val, max_val):
        return 0 <= val < max_val

    def dfs(self, row, col, matrix, length, cache):
        rows = len(matrix)
        cols = len(matrix[0])

        best_length = length
        deltas = [[0, -1], [-1, 0], [0, +1], [+1, 0]]

        for [drow, dcol] in deltas:
            next_row = row + drow
            next_col = col + dcol
            if not self.in_range(next_row, rows) or not self.in_range(next_col, cols):
                continue

            if matrix[row][col] >= matrix[next_row][next_col]:
                continue

            new_length = 0
            if cache[next_row][next_col] is not 0:
                new_length = cache[next_row][next_col]
            else:
                new_length = self.dfs(next_row, next_col, matrix, 1, cache)
            new_length += length
            best_length = max(best_length, new_length)


        cache[row][col] = best_length
        return best_length

    def longestIncreasingPath(self, matrix):
        if matrix is None:
            return 0
        rows = len(matrix)
        if rows is 0:
            return 0
        cols = len(matrix[0])
        if cols is 0:
            return 0
        best_length = -1
        cache = [[0] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                new_length = cache[row][col]
                if new_length == 0:
                    new_length = self.dfs(row, col, matrix, 1, cache)
                best_length = max(best_length, new_length)

        return best_length

sol = Solution()

print(sol.longestIncreasingPath([
        irint_matrix(matrix)
  [9,9,4],
  [6,6,8],
  [2,1,1]
]))

print('')
        irint_matrix(matrix)
print('')
print('')

print(sol.longestIncreasingPath([
  [3,4,5],
  [3,2,6],
  [2,2,1]
]))

