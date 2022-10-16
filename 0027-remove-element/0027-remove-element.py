class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for _ in range(sum([1 for x in nums if x == val])):
            nums.remove(val)
        return len(nums)