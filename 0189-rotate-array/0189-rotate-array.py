class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        while k > 0:
            temp = nums[-1]
            del nums[-1]
            nums.insert(0, temp)
            k -= 1
        