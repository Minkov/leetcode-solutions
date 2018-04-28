class Solution:
    def get_words(self, text):
        words = []
        word = []
        for ch in text:
            if not ch.isalpha():
                if len(word) > 0:
                    words.append("".join(word).lower())
                word = []
            else:
                word.append(ch)
        if len(word) > 0:
                words.append("".join(word).lower())
        return words

    def get_most_common_word(self, words):
        words_counts = dict()
        for word in words:
            if word not in words_counts:
                words_counts[word] = 0
            words_counts[word] += 1
        most_common_word = ''
        most_common_word_count = -1
        for word, count in words_counts.items():
            if count > most_common_word_count:
                most_common_word_count = count
                most_common_word = word

        return most_common_word

    def mostCommonWord(self, paragraph, banned):
        banned = set(banned)
        counts = dict()
        words = self.get_words(paragraph)
        print(words)
        words = filter(lambda word: word not in banned, words)
        most_common_word = self.get_most_common_word(words)
        return most_common_word


sol = Solution()
print(sol.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
print(sol.mostCommonWord("Bob. hIt, baLl", ["bob", "hit"]))
