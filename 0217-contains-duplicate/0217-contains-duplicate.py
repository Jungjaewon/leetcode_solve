class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        solve_dict = dict()
        for n in sorted(nums):
            if n not in solve_dict:
                solve_dict[n] = 0
            solve_dict[n] += 1
            
            if solve_dict[n] >= 2:
                return True
        return False