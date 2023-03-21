class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        ans_l = [0,0]
        for i in range(32):
            if i & 1 == 0 and n & 1 << i:
                ans_l[0] += 1
            elif i & 1 != 0 and n & 1 << i:
                ans_l[1] += 1
        return ans_l
            