class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s,e = 0, len(nums) - 1
        while s <= e:
            mid = (s + e) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                s,e = mid + 1,e
            elif nums[mid] > target:
                s,e = s,mid - 1
        return -1