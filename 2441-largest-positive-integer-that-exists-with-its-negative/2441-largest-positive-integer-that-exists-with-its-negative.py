class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        """
        for n in sorted(nums)[::-1]:
            if -n in nums:
                return n
        return -1
        """
        """
        a_dict, ans = defaultdict(list), -1
        for n in nums:
            a_dict[abs(n)].append(n)
        for n in a_dict:
            if len(a_dict[n]) >= 2 and n in a_dict[n] and -n in a_dict[n]:
                ans = max(ans, n)
        return ans
        """
        a_set, ans = set(), -1
        for n in nums:
            a_set.add(n)
        for n in nums:
            if n in a_set and -n in a_set:
                ans = max(ans, n)
        return ans