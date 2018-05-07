class Solution:
    def is_completing(self, word, chars):
        i = 0
        j = 0
        while i < len(chars) and j < len(word):
            if chars[i] == word[j]:
                i += 1
                j += 1
            else:
                i += 1
        return j == len(word)
    def shortestCompletingWord(self, licensePlate, words):
        license_chars = ''.join(sorted([c.lower() for c in licensePlate if c.isalpha()]))
        print(license_chars)
        best_word = 'x' * 16
        for word in words:
            check_word = ''.join(sorted(word))
            if len(check_word) < len(best_word) and self.is_completing(license_chars, check_word):
                best_word = word
        return best_word
sol = Solution()


print(sol.shortestCompletingWord("1s3 PSt", [
      "step", "steps", "stripe", "stepple"]))
print(sol.shortestCompletingWord("1s3 456", ["looks", "pest", "stew", "show"]))
