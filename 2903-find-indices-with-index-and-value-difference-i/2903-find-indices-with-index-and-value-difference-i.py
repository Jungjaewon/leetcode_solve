class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        """
        ans = [-1, -1]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(i - j) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]
        return ans
        """
        """
        ans = [-1, -1]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(i - j) >= indexDifference:
                    if abs(nums[i] - nums[j]) >= valueDifference:
                        return [i, j]
        return ans
        """
        """
        ans = [-1, -1]
        for i in range(len(nums)):
            for j in range(indexDifference, len(nums)):
                if abs(i - j) >= indexDifference:
                    if abs(nums[i] - nums[j]) >= valueDifference:
                        return [i, j]
        return ans
        """
        """
        ans = [-1, -1]
        for i in range(len(nums)):
            for j in range(indexDifference + i, len(nums)):
                if abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]
        return ans
        """
        ans = [-1, -1]
        for i in range(len(nums)):
            for j in range(0, len(nums)):
                if abs(i - j) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]
        return ans