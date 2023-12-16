class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_list, t_list = list(s)[::-1], list(t)[::-1]
        s_result = list()
        cnt = 0
        for c in s_list:
            if c == '#':
                cnt += 1
            else:
                if cnt:
                    cnt -= 1
                    continue
                s_result.append(c)
        t_result = list()
        cnt = 0
        for c in t_list:
            if c == '#':
                cnt += 1
            else:
                if cnt:
                    cnt -= 1
                    continue
                t_result.append(c)
        return ''.join(s_result[::-1]) == ''.join(t_result[::-1])
        