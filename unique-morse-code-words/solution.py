class Solution:
    def get_morse_code(self, letter):
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        code = ord(letter) - ord('a')
        return codes[code]


    def encode(self, word):
        result = []
        for letter in word:
            result.append(self.get_morse_code(letter))
        return "".join(result)

    def uniqueMorseRepresentations(self, words):
        word_codes = set()
        for word in words:
            word_code = self.encode(word)
            word_codes.add(word_code)

        return len(word_codes)


sol = Solution()

print(sol.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))

