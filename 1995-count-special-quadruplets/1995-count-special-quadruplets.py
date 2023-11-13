class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        """
        ans = 0
        for a in range(len(nums)):
            for b in range(a + 1, len(nums)):
                for c in range(b + 1, len(nums)):
                    for d in range(c + 1, len(nums)):
                        if nums[a] + nums[b] + nums[c] == nums[d]:
                            ans += 1
        return ans
        """
        ans = 0 
        check_dict = defaultdict(int)
        for a in range(len(nums)-1,-1,-1):
            check_dict[nums[a]] += 1
            for b in range(a-1,-1,-1):
                for c in range(b-1,-1,-1):
                    temp_sum = nums[a] + nums[b] + nums[c]
                    if temp_sum in check_dict:
                        ans += check_dict[temp_sum]
        return ans
    #https://leetcode.com/problems/count-special-quadruplets/discuss/1456709/Python-99-Clean-Code-Walkthrough-From-O(4)-greater-O(3)-greater-O(2)