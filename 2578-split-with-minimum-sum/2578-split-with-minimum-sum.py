class Solution:
    def splitNum(self, num: int) -> int:
        num_list = [ x for x in list(str(num))]
        num_list.sort(key=lambda x : int(x))
        num1, num2 = list(), list()
        for idx, n in enumerate(num_list):
            if idx & 1 == 0:
                num1.append(n)
            else:
                num2.append(n)
        return int(''.join(num1)) + int(''.join(num2))
    # return int((w:=''.join(sorted(str(num))))[::2])+int(w[1::2])
    # https://leetcode.com/problems/split-with-minimum-sum/discuss/4825375/Python-one-line-solution