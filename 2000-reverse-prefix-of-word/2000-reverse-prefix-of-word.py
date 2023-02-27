class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        """
        if ch not in word:
            return word
        else:
            idx = word.index(ch)
            ret = word[:idx + 1]
            return word.replace(ret, ret[::-1])
        """
        """
        if ch not in word:
            return word
        else:
            ret = word[:word.index(ch) + 1]
            return word.replace(ret, ret[::-1])
        """
        """
        if ch not in word:
            return word
        else:
            return word.replace(word[:word.index(ch) + 1], word[:word.index(ch) + 1][::-1])
        """
        return word if ch not in word else word.replace(word[:word.index(ch) + 1], word[:word.index(ch) + 1][::-1])