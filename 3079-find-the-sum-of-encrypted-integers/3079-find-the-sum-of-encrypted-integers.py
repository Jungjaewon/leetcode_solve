class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        for idx in range(len(nums)):
            converted_x = str(nums[idx])
            max_v = max(list(map(int, converted_x)))
            nums[idx] = int(str(max_v) * len(converted_x))
        return sum(nums)