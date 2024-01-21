class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for i in range(1, len(nums) + 1):
            temp = list(itertools.combinations(nums, i))
            temp = [list(temp) for x in temp][0]
            #print(temp)
            ans.extend(temp)
        return ans