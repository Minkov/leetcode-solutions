
class Solution:
    def repeatedSubstringPattern(self, s):
        len_s = len(s)
        for current_len in range(1, len_s // 2 + 1):
            if len_s % current_len > 0:
                continue
            repeated_s = s[:current_len] * (len_s // current_len)
            if repeated_s == s:
                return True
        return False

sol = Solution()

print("abab", sol.repeatedSubstringPattern("abab"))
print("aba", sol.repeatedSubstringPattern("aba"))
print("abcabcabcabc", sol.repeatedSubstringPattern("abcabcabcabc"))

