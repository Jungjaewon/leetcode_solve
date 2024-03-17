class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        else:
            pos,temp_list = 0, list()
            for c in t:
                if s[pos] != c:
                    continue
                else:
                    temp_list.append(c)
                    if pos + 1 != len(s):
                        pos +=1
            if s in ''.join(temp_list):
                return True
            else:
                return False
        