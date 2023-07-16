class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def word2int(word):
            return int(''.join([str(ord(c) - ord('a')) for c in word]))
        return word2int(firstWord) + word2int(secondWord) == word2int(targetWord)