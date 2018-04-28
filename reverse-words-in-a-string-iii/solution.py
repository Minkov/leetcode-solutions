class Solution:
    def reverseWords(self, s):
        words = s.split(' ')
        fixed_words = []
        for word in words:
            word = list(word)
            word.reverse()
            word = ''.join(word)
            fixed_words.append(word)

        fixed_words = ' '.join(fixed_words)
        return fixed_words
        
sol = Solution()

print(sol.reverseWords("Let's take LeetCode contest"))
