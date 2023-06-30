class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans, c_words = list(), [dict(Counter(word)) for word in words]
        for c in c_words[0]:
            num, flag = c_words[0][c], True
            for idx in range(1, len(c_words)):
                word_dict = c_words[idx]
                if c not in c_words[idx]:
                    flag = False
                    break
                elif num > c_words[idx][c]:
                    num = c_words[idx][c]
                    #flag = False
                    #break
            if flag:
                for _ in range(num):
                    ans.append(c)
        return ans