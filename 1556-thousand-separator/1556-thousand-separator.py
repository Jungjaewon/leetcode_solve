class Solution:
    def thousandSeparator(self, n: int) -> str:
        n_list = list(str(n))
        ans,cnt = list(), 0
        for i in n_list[::-1]:
            if cnt == 3:
                ans.append('.')
                ans.append(i)
                cnt = 1
            else:
                ans.append(i)
                cnt += 1
        return ''.join(ans)[::-1]