class Solution:
    def checkString(self, s: str) -> bool:
        """
        c_dict = dict(Counter(s))
        if 'a' not in c_dict:
            return True
         
        for c in s:
            if c == 'a':
                c_dict[c] -= 1
            elif c == 'b' and c_dict['a'] == 0:
                c_dict[c] -= 1
            else:
                return False
        return True
        """
        if 'a' not in s:
            return True
        
        c_dict = dict(Counter(s))
         
        for c in s:
            if c == 'a':
                c_dict[c] -= 1
            elif c == 'b' and c_dict['a'] == 0:
                c_dict[c] -= 1
            else:
                return False
        return True
        