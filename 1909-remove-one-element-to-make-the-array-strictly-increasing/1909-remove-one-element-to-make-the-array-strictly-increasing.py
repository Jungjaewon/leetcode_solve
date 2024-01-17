class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        ans = list()
        for i in range(len(nums)):
            new_arr = nums[:i] + nums[i + 1:]
            flag = True
            for j in range(len(new_arr) - 1):
                if not (new_arr[j] < new_arr[j + 1]):
                    flag = False
                    break
            ans.append(flag)
        return any(ans)