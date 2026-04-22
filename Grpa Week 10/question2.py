class StringManipulation:
    def __init__(self, words):
        self.words = words

    def total_words(self):
        return len(self.words)

    def count(self, some_word):
        return self.words.count(some_word)

    def words_of_length(self, length):
        return [word for word in self.words if len(word) == length]

    def words_start_with(self, char):
        return [word for word in self.words if word.startswith(char)]

    def longest_word(self):
        if not self.words:
            return ""
        return max(self.words, key=len)

    def palindromes(self):
        return [word for word in self.words if word == word[::-1]]
