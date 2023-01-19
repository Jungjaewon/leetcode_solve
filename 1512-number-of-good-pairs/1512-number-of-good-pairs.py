class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans_dict, ans = defaultdict(int), 0
        """
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    ans += 1
        return ans
        """
        for n in nums:
            ans_dict[n] += 1
        for key in ans_dict:
            n = ans_dict[key]
            ans += n * (n + 1) / 2 - n 
        return int(ans)