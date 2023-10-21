class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        """
        a = "qwertyuiop"
        b = "asdfghjkl"
        c = "zxcvbnm"
        ans = list()
        for row in [a,b,c]:
            for word in words:
                flag = True
                for c in word:
                    if c.lower() not in row:
                        flag = False
                        break
                if flag:
                    ans.append(word)
        return ans
        """
        a = set("qwertyuiop")
        b = set("asdfghjkl")
        c = set("zxcvbnm")
        ans = list()
        for row in [a,b,c]:
            for word in words:
                flag = True
                for c in word:
                    if c.lower() not in row:
                        flag = False
                        break
                if flag:
                    ans.append(word)
        return ans