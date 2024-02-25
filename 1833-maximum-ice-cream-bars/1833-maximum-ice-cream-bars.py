class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        """
        costs, ans = sorted(costs), 0
        for c in costs:
            if c <= coins:
                coins -= c
                ans += 1
        return ans
        """
        # https://leetcode.com/problems/maximum-ice-cream-bars/discuss/3006066/One_liner.py
        return sum(1 for icecream in sorted(costs) if (coins:= coins-icecream) >= 0)
            
        
        