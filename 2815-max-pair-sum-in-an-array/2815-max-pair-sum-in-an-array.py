class Solution:
    def maxSum(self, nums: List[int]) -> int:
        """
        ans = -1
        for a, b in list(combinations(nums, 2)):
            if sorted(list(str(a)))[-1] == sorted(list(str(b)))[-1]:
                ans = max(ans, a + b)
        return ans
        """
        """
        ans = -1
        for a, b in list(combinations(nums, 2)):
            if max(list(str(a))) == max(list(str(b))):
                ans = max(ans, a + b)
        return ans
        """
        ans = -1
        a_dict = defaultdict(list)
        for num in nums:
            a_dict[max(list(str(num)))].append(num)
        max_key = sorted(list(a_dict.keys()))[-1]
        for n in a_dict:
            if len(a_dict[n])> 1:
                for a,b in list(combinations(a_dict[n],2)):
                    ans = max(ans, a + b)
        return ans