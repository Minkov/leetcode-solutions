class Solution:
    def searchMatrix(self, matrix, target):
        def to_row_col(value, coeff):
            return [value// coeff, value % coeff]
        def to_value(x, y, coeff):
            return x * coeff + y

        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        n = len(matrix)
        m = len(matrix[0])
        if not n or not m:
            return False
        coeff = m
        l = 0
        r = to_value(n - 1, m - 1, coeff)
        while l < r:
            mid = (l + r) // 2
            [row, col] = to_row_col(mid, coeff)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = to_value(row, col, coeff) + 1
            else:
                r = to_value(row, col, coeff)
        if l == r:
            [row, col] = to_row_col(l, coeff)
            return matrix[row][col] == target
        return False


print(Solution().searchMatrix([[1]], 1))
print(Solution().searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 3))

print(Solution().searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 13))