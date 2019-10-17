class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0
        n = len(name)
        m = len(typed)
        while i < n and j < m:
            if name[i] == typed[j]:
                i += 1
                j +=1
            else:
                j +=1
        return i == n

tests = [
    ["alex", "aaleex", True],
    ["saeed", "ssaaedd", False],
    ["leelee", "lleeelee", True],
    ["laiden", "laiden", True]
]

for [name, typed, expected] in tests:
    print(name, typed)
    actual = Solution().isLongPressedName(name, typed)
    print(expected, actual)
    print('-' * 10)