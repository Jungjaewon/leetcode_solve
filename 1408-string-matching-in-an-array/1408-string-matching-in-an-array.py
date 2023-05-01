class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = set()
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                elif words[i] in words[j]:
                    ans.add(words[i])
        return list(ans)
