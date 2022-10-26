from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        rn_dict, mag_dict = dict(Counter(ransomNote)), dict(Counter(magazine))
        
        for c in sorted(rn_dict.keys()):    
            if c not in mag_dict:
                return False
            elif not (rn_dict[c] <= mag_dict[c]):
                return False    
        return True
        
        
        