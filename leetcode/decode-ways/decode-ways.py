# class Solution:
#     def numDecodings(self, s: str) -> int:
#         def rec(s):
#             n = len(s)
#             if n == 0:
#                 return 1
#             if s[0] == '0':
#                 return 0
#             total = 0
#             if n > 1:
#                 if s[0] == '1':
#                     total += rec(s[2:])
#                 if s[0] == '2' and s[1] in ['0', '1', '2', '3', '4', '5', '6']:
#                     total += rec(s[2:])
#             total += rec(s[1:])
#             return total
#         if len(s) > 0 and s[0] == '0':
#             return 0
#         return rec(s)

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0 or s[0] == '0':
            return 0
        if n == 2 and '0' in s:
            return 1

        d = [0] * n
        d[0] = 0
        for i in range(1, n):
            if s[i-1] == '0':
                if s[i] == '0':
                    return 0
                d[i] = d[i-1]
            else:
                if s[i - 1] in ['1', '2']:
                    d[i] += 1
                if s[i-1] == '2' and s[i] in ['7', '8', '9']:
                    d[i] -= 1
                if s[i] == '0':
                    d[i] -= 1
                d[i] += d[i-1]
        if s[-1] != '0':
            d[-1] += 1
        return d[-1]

tests = [
    ['99', 1],
    ['27', 1],
    ['0', 0],
    ['100', 0],
    ['110', 1],
    ['10', 1],
    ['12', 2],
    ['101', 1],
    ['01', 0],
    ['226', 3],
    ['1010', 1],
]

for [input, answer] in tests:
    print('-' * 10)
    print(input, Solution().numDecodings(input), answer )
    print('-' * 10)
