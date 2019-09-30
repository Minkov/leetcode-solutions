from sys import maxsize

class Solution:
    def numSquares(self, n: int) -> int:
        def get_squares(num):
            squares = []
            current = 1
            while current ** 2 <= num:
                squares.append(current * current)
                current += 1
            return squares

        def find_min_count(num, values):
            if num == 0:
                return 0
            current = maxsize
            for value in values:
                if value > num:
                    continue
                if num - value == 0:
                    return 1
                current = min(
                    current,
                    1 + find_min_count(num - value, values)
                )
            return current
        return find_min_count(n, sorted(get_squares(n), reverse=True))

# 51 = 49 + 1 + 1




# print(Solution().numSquares(12))
# print(Solution().numSquares(13))
# print(Solution().numSquares(16))
print(Solution().numSquares(41))
print(Solution().numSquares(51))