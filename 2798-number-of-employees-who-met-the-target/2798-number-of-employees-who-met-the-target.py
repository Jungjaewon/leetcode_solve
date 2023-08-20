class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        """
        ans = 0
        for h in hours:
            if target <= h:
                ans += 1
        return ans
        """
        return sum([1 for h in hours if target <= h])
