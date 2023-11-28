class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = list()
        for idx , word in enumerate(words):
            if x in word:
                ans.append(idx)
        return ans