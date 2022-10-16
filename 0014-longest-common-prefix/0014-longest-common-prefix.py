class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        first_s = strs[0]
        for idx in range(len(first_s)):
            
            s, flag = first_s[:idx + 1], True
            
            for i in range(1, len(strs)):
                if s != strs[i][:idx + 1]:
                    flag = False
                    break
            
            if not flag:
                return first_s[:idx]
        
        return first_s
        
            