class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        for k in range(2, 3):
            for items in list(itertools.combinations(nums,k)):
                temp, flag = 0, False
                for n in items:
                    if n & 1 == 1:
                        flag = True
                        break
                    temp = temp | n                    
                if flag:
                    continue
                    
                if bin(temp)[-1:] == '0' or bin(temp)[-2:] == '10' or bin(temp)[-3:] == '110':
                    return True
        return False