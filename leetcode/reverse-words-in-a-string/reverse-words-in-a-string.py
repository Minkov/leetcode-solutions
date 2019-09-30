class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(list(filter(lambda x: x, s.split(' ')))[::-1])
tests = [
    ["the sky is blue", "blue is sky the"],
    ["  hello world!  ", "world! hello"],
    ["a good   example", "example good a"]
]

solution = Solution()
for [input, expected] in tests:
    actual = solution.reverseWords(input)
    print(actual, expected, actual == expected)