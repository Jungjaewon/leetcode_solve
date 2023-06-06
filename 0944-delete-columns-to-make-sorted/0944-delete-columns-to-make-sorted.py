class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        """
        ans = 0
        col_list = list(zip(*strs))
        for col in col_list:
            if list(col) != sorted(col):
                ans += 1
        return ans
        """
        return sum([1 for col in list(zip(*strs)) if list(col) != sorted(col)])
        
        
        