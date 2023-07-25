class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        """
        ans = list()
        for word in words:
            ans.extend(word.split(separator))
            ans = [a for a in ans if a != ""]
        return ans
        """
        ans = list()
        for word in words:
            for w in word.split(separator):
                if w != "":
                    ans.append(w)
        return ans
        