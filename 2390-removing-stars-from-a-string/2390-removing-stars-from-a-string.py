class Solution:
    def removeStars(self, s: str) -> str:
        """
        f_i = s.find('*')
        while f_i != -1:
            s = f'{s[ :f_i - 1]}{s[f_i + 1:]}'
            #print(s, f_i)
            f_i = s.find('*')
        return s
        """
        ans = list()
        for c in s:
            if c == '*':
                ans.pop()
            else:
                ans.append(c)
        return ''.join(ans)
        
                
                
                
                
                
        
        