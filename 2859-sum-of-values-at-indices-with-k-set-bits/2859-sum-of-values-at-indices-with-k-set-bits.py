class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans = 0
        for idx, n in enumerate(nums):
            cnt = 0
            for i in range(32):
                if idx & 1 << i:
                    cnt += 1
            if cnt == k:
                ans += n
        return ans
            
            