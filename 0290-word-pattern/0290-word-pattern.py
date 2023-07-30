class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list_s = list(set(s.split()))
        list_p = list(set(pattern))
        
        if (len(list_p) != len(list_s)) or len(pattern) != len(s.split()):
            return False
        else:
            a_dict = dict()
            for c, w in zip(pattern, s.split()):
                if w not in a_dict:
                    a_dict[w] = c
                elif w in a_dict and c != a_dict[w]:
                    return False
            return True
                