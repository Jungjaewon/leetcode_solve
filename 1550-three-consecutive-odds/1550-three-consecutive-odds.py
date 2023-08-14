class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cnt = 0
        for n in arr:
            if cnt == 3:
                return True
            if n & 1:
                cnt += 1
            else:
                cnt = 0
        return cnt == 3