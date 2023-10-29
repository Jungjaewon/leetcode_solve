class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        pos_int = list(range(1, 2001))
        arr_set = set(arr)
        ans = list()
        for n in pos_int:
            if n not in arr_set:
                ans.append(n)
        return ans[k - 1]
        
        