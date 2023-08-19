class Solution:
    def finalString(self, s: str) -> str:
        ans = list()
        for c in s:
            if c == 'i':
                ans = ans[::-1]
            else:
                ans.append(c)
        return ''.join(ans)