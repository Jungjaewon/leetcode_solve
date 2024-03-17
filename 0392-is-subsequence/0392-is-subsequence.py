class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
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
        """
        """
        slow = 0
        if len(s) == 0:
            return True
        for fast in range(len(t)):
            if s[slow] == t[fast]:
                slow += 1
            if slow == len(s):
                return True
        return False
        # https://leetcode.com/problems/is-subsequence/discuss/4738906/98-VERY-EASY-oror-Slow-and-Fast-pointer-solution
        """
        if s == "":
            return True
        else:
            def func(s, t, s_l, t_l):
                if s_l == -1:
                    return True
                if t_l == -1:
                    return False
                if s[s_l] == t[t_l]:
                    return func(s, t, s_l -1, t_l -1)
                else:
                    return func(s, t, s_l, t_l -1)
            return func(s, t, len(s) - 1, len(t) - 1)