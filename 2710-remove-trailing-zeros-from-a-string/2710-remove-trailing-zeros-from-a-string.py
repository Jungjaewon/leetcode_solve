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
        """
        return num.rstrip('0')
        """
        n_list = list(num)
        for idx in range(len(n_list) - 1, 0,-1):
            if n_list[idx] == '0':
                n_list[idx] = ''
            else:
                break
        return ''.join(n_list)
        