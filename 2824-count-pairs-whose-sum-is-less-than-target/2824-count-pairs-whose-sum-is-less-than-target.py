class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        """
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if i != j and nums[i] + nums[j] < target:
                    ans +=1
        return ans
        """
        """
        ans = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] < target:
                    ans +=1
        return ans // 2
        """
        #return sum([1 for i in range(len(nums)) for j in range(i + 1, len(nums)) if i != j and nums[i] + nums[j] < target])
        # https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/discuss/3934543/Python-3-oror-1-line-combinations-oror-TM%3A-54-ms-16-MB
        #return sum(map(lambda x: x[0]+x[1] < target, combinations(nums, 2)))
        #https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/discuss/3937200/Python-Elegant-and-Short-or-Brute-Force-vs-Greedy-or-O(n*log(n))
        nums.sort()

        lo, hi = 0, len(nums) - 1
        pairs = 0

        while lo < hi:
            if nums[lo] + nums[hi] < target:
                pairs += hi - lo
                lo += 1
            else:
                hi -= 1

        return pairs