class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        """
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    ans += 1
        return ans
        """
        # https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/discuss/1471015/Python-Clean-and-concise.-Dictionary-T.C-O(N)
        # https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/discuss/2552609/Python-Faster-than-99
        ans, seen = 0, defaultdict(int)
        for n in nums:
            seen[n] += 1
            ans += seen[n - k] + seen[n + k]
        return ans