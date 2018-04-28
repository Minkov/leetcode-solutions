class Solution:
    def numberOfLines(self, widths, S):
        lines = 0
        current_width = 0
        for letter in S:
            index = ord(letter) - ord('a')
            letter_width = widths[index]
            if current_width + letter_width > 100:
                lines += 1
                current_width = 0
            current_width += letter_width
        return [lines + 1, current_width]


sol = Solution()

print(sol.numberOfLines([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "abcdefghijklmnopqrstuvwxyz"))
print(sol.numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "bbbcccdddaaa"))
