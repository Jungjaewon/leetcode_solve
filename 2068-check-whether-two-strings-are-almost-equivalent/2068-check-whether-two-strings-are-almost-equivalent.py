class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        w1_c, w2_c = dict(Counter(word1)), dict(Counter(word2))
        most_d = -10e4
        for c in set(word1) | set(word2):
            print(abs(w1_c.get(c,0) -  w2_c.get(c,0)))
            most_d = max(most_d, abs(w1_c.get(c,0) -  w2_c.get(c,0)))
        return most_d <= 3
        
        