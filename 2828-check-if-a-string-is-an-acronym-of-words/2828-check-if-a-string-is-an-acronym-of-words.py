class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        """
        return ''.join([ w[0] for w in words]) == s
        """
        ans = list()
        for w in words:
            ans.append(w[0])
        return ''.join(ans) == s