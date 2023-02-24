class Solution:
    def replaceDigits(self, s: str) -> str:
        s_list = list(s)
        for i in range(1, len(s_list)):
            c = s_list[i]
            if '0' <= c and c <= '9':
                s_list[i] = chr(ord(s_list[i - 1]) + int(c))
        return ''.join(s_list)