class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        cnt = Counter()
        for word in words:
            cnt += Counter(word)
        n = len(words)
        for key in cnt:
            freq = cnt[key]
            if freq % n != 0:
                return False
        return True
        