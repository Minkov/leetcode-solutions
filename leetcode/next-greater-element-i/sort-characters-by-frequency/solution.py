class Solution:
    def frequencySort(self, s):
        by_frequencies = dict()
        for ch in s:
            if ch not in by_frequencies:
                by_frequencies[ch] = 0
            by_frequencies[ch] += 1
        chars = [[by_frequencies[ch], ch] for ch in s]
        chars = sorted(chars, reverse=True)
        return ''.join(ch for [_, ch] in chars)

sol = Solution()

print(sol.frequencySort("tree"))
print(sol.frequencySort("cccaaa"))
print(sol.frequencySort("Aabb"))

