class Solution:
    def isSubsequence(self, s, t):
        # s is the small
        s_len = len(s)
        t_len = len(t)
        if t_len < s_len:
            return False
        if t_len == s_len:
            return s == t
        t_index = 0

        letters_found = 0

        for i in range(s_len):
            letter = s[i]
            while t_index < t_len and letter != t[t_index]:
                t_index += 1
            if t_index == t_len:
                break
            t_index += 1
            letters_found += 1
        return letters_found == s_len

sol = Solution()

print(sol.isSubsequence("abc", "ahbgdc"))
print(sol.isSubsequence("axc", "ahbgdc"))
print(sol.isSubsequence("a", "b"))
print(sol.isSubsequence("acb", "ahbgdc"))

