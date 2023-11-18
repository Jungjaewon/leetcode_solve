class Solution:
    def countOdds(self, low: int, high: int) -> int:
        t = high - low + 1
        if t & 1 == 0:
            return t // 2
        else:
            if low & 1 == 1 and high & 1 == 1:
                return (t // 2) + 1
            elif (low & 1 == 0 and high & 1 == 1) or (low & 1 == 1 and high & 1 == 0):
                return (t // 2) + 1
            elif low & 1 == 0 and high & 1 == 0:
                return t // 2
            
        """
        cnt = 0
        for i in range(low, high + 1):
            if i & 1 == 1:
                cnt += 1
        return cnt
        """