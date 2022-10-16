class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        idx2num_dict, num2idx_dict = dict(), dict()
        for i, d in enumerate(nums):
            idx2num_dict[i] = d
            
            if d not in num2idx_dict:
                num2idx_dict[d] = list()
            num2idx_dict[d].append(i)
        
        for i, d in enumerate(nums):
            
            res = target - d
            
            if res == d and len(num2idx_dict[d]) == 1:
                continue
            
            if res in num2idx_dict:
                ans = [i]
                
                for a in num2idx_dict[res]:
                    if a != i:
                        return[i, a]