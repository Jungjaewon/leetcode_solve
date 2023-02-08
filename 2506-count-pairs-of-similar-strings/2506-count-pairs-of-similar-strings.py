class Solution:
    def similarPairs(self, words: List[str]) -> int:
        ans = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                    if i != j and set(words[i]) == set(words[j]):
                        ans += 1
        return ans