class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost = sorted(cost)
        ans = 0
        while len(cost):
            if len(cost) >= 3:
                ans += cost[-1] + cost[-2]
                cost = cost[:-3]
            elif len(cost) == 2:
                ans += cost[-1] + cost[-2]
                cost = cost[:-2]
            else:
                ans += sum(cost)
                cost = []
        
        return ans