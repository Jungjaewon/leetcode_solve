class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        """
        n_list, cnt = list(num)[::-1], 0
        for s in n_list:
            if s == '0':
                cnt += 1
            else:
                break
        return ''.join(n_list[cnt:][::-1])
        """
        return num.rstrip('0')