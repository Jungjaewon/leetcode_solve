from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s_dict = defaultdict(int)
        for n in nums:
            s_dict[n] += 1
        ans, cnt = 0, 0
        for n in s_dict:
            if s_dict[n] > cnt:
                ans = n
                cnt = s_dict[n]
        return ans
        