class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        #return [n for n in nums if n & 1 == 0] + [n for n in nums if n & 1 == 1]
        nums.sort(key=lambda x : x % 2)
        return nums