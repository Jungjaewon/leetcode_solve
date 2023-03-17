class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while not len(s) <= k:
            temp_list = list()
            loop = len(s) // k if len(s) % k == 0 else len(s) // k + 1
            for _ in range(loop):
                s_i = s[:k]
                s = s[k:]
                temp_list.append(str(sum([int(i) for i in s_i])))
            s = ''.join(temp_list)
        return s