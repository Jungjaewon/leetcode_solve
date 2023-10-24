class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        ans = list()
        def check(s):
            s_l = len(s)
            s_i, e_l = 0, s_l - 1
            mid = s_l // 2
            while s_i < e_l:
                if s[s_i] != s[e_l]:
                    return False
                s_i += 1
                e_l -= 1
            if s_l & 1 == 1:
                pass
            else:
                pass
            return True
        for word in words:
            if check(word):
                ans.append(word)
        #return sorted(ans)[0] if len(ans) else ""
        return ans[0] if len(ans) else ""