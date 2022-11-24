class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        temp, idx = "", 0
        while idx < len(s):
            temp += s[idx]
            if part in temp:
                temp = temp.replace(part, "")
            idx += 1
        return temp
        #Ref:https://leetcode.com/problems/remove-all-occurrences-of-a-substring/discuss/1373251/PYTHON-FOR-BEGINNERS
        """
        while part in s:
            s = s.replace(part, '', 1)
        return s
        """
        """
        ### Time Limit
        while part in s:
            ans, idx = list(), 0
            while idx < len(s):
                #print(f'{part}, {s[idx:idx+ len(part)]}, {part == s[idx:idx+ len(part)]}')
                if part == s[idx:idx + len(part)]:
                    idx += len(part)
                else:
                    #print(f'false idx : {idx}')
                    ans.append(s[idx])
                    idx += 1
                if len(ans):
                    for c in s:
                        ans.append(c)
                    s = ''.join(ans)
                    ans, idx = list(), 0
            s = ''.join(ans)
            #print(s)
        return s
        
        """