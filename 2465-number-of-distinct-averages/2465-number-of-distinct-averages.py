class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        
        if len(nums) == 2:
            return 1
        else:
            ans = set()
            while len(nums):
                x_min = min(nums)
                nums.remove(x_min)
                x_max = max(nums)
                nums.remove(x_max)
                ans.add((x_min + x_max) / 2)
            #counter = Counter(ans)
            #print(counter)
            return len(ans)
            