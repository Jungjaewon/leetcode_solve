class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        s_cnt,t_cnt, ans = Counter('balloon'), Counter(text), list()
        for c in s_cnt:
            if c in t_cnt:
                ans.append(t_cnt[c] // s_cnt[c])
            else:
                ans.append(0)
        return min(ans)
        
        
        