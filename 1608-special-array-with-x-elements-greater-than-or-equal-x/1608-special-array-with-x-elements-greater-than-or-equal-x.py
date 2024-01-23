class Solution:
    def specialArray(self, nums: List[int]) -> int:
        """
        for i in range(1, 1001):
            base = [ x for x in nums if x >= i]
            if len(base) == i:
                return i
        return -1
        """
        for i in range(1, 101):
            base = [ x for x in nums if x >= i]
            if len(base) == i:
                return i
        return -1