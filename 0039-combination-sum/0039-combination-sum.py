import queue
import copy

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        Q, ans, ret = queue.Queue(), list(), list()
        
        for c in candidates:
            Q.put([c])
            
        while Q.qsize():
            temp = Q.get()
            temp_sum = sum(temp)
            
            if temp_sum == target:
                ans.append(temp)
            else:
                for c in candidates:
                    if not temp_sum + c > target:
                        #temp_copy = copy.deepcopy(temp)
                        #temp_copy.append(c)
                        Q.put([*temp, c])
                        
        ans = [sorted(x) for x in ans]
        for candi in ans:
            if candi not in ret:
                ret.append(candi)
        return ret