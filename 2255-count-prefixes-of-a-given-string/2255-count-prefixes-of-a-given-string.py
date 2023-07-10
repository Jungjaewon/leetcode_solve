class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        """
        cnt = 0
        for word in words:
            cnt = cnt + 1 if word in s[:len(word)] else cnt
        return cnt
        """
        return sum([1 if word in s[:len(word)] else 0 for word in words])