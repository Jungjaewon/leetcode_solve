class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        """
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        ans += 1
        return ans
        """
        """
        ans, temp_set = 0, set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] - nums[i] == diff:
                    temp_set.add(f'{i}_{j}')
        for s in temp_set:
            i, j = [int(x) for x in s.split('_')]
            for k in range(j + 1, len(nums)):
                if nums[k] - nums[j] == diff:
                    ans += 1
        return ans
        """
        ans, temp_set = 0, set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] - nums[i] == diff:
                    temp_set.add(j)
        for j in temp_set:
            for k in range(j + 1, len(nums)):
                if nums[k] - nums[j] == diff:
                    ans += 1
        return ans