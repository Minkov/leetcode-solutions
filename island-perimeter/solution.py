class Solution:
    def find_one(self, grid):
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] is 1:
                    return [row, col]
        return []

    def in_range(self, value, max_value):
        return 0 <= value < max_value

    def islandPerimeter(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        cells = [self.find_one(grid)]
        deltas = [[0, -1], [-1, 0], [0, +1], [+1, 0]]
        visited = set()
        visited.add('%d;%d' % (cells[-1][0], cells[-1][1]))
        walls = 0

        while len(cells) > 0:
            [row, col] = cells.pop()
            for [drow, dcol] in deltas:
                next_row = row + drow
                next_col = col + dcol
                if not self.in_range(next_row, rows) or not self.in_range(next_col, cols):
                    walls += 1
                    continue
                if grid[next_row][next_col] == 0:
                    walls += 1
                    continue
                visited_code = '%d;%d' % (next_row, next_col)
                if visited_code in visited:
                    continue
                visited.add(visited_code)
                cells.append([next_row, next_col])

        return walls


print(Solution().islandPerimeter([[1]]))
print(Solution().islandPerimeter([[1, 1], [1, 1]]))
print(Solution().islandPerimeter([[0, 1, 0, 0],
                                  [1, 1, 1, 0],
                                  [0, 1, 0, 0],
                                  [1, 1, 0, 0]]))
