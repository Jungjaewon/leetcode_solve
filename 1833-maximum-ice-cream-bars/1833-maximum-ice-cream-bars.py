class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs, ans = sorted(costs), 0
        for c in costs:
            if c <= coins:
                coins -= c
                ans += 1
        return ans
            
        
        