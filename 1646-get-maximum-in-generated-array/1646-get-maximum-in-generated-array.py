class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            nums = [0] * (n + 1)
            nums[0], nums[1] = 0, 1
            for i in range(n + 2):
                if 2 <= 2 * i and 2 * i <= n:
                    nums[2 * i] = nums[i]

                if 2 <= 2 * i + 1 and 2 * i + 1 <= n:
                    nums[2 * i + 1] = nums[i] + nums[i + 1]
            #print(nums)
            return max(nums)
        