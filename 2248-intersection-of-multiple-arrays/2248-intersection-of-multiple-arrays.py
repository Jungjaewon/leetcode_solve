class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        nums_set  = [set(n) for n in nums]
        temp_set = nums_set[0]
        for n_s in nums_set[1:]:
            temp_set = temp_set.intersection(n_s)
        return sorted(list(temp_set))
            