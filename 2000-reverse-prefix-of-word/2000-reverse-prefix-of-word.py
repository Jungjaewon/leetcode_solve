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
        if ch not in word:
            return word
        else:
            ret = word[:word.index(ch) + 1]
            return word.replace(ret, ret[::-1])