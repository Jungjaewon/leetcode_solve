class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        def func(a, b):
            if a in [None, ""] or b in [None, ""]:
                return ""
            ans = ""
            print(a, b)
            for idx in range(min(len(a), len(b))):
                
                if a[idx] == b[idx]:
                    ans += a[idx]
                else:
                    break
            return ans
            
        ans = strs[0]
        for idx in range(1, len(strs)):
            ans = func(ans, strs[idx])
        return ans