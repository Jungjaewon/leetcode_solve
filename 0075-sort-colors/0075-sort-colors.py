class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red, white, blue, idx = 0,0,0,0
        for num in nums:
            if num == 0:
                red += 1
            elif num == 1:
                white += 1
            elif num == 2:
                blue += 1
        for _ in range(red):
            nums[idx] = 0
            idx += 1
        for _ in range(white):
            nums[idx] = 1
            idx += 1
        for _ in range(blue):
            nums[idx] = 2
            idx += 1
        #nums.sort()
        