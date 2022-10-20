class Solution:
    def arrangeCoins(self, n: int) -> int:
        cnt = 1
        while True:
            
            if n >= cnt:
                n = n - cnt
                cnt += 1
            else:
                break
        return cnt -1