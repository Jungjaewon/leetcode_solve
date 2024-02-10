class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        """
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
        """
        """
        cost, ans = sorted(cost)[::-1], 0
        for i in range(len(cost)):
            if (i + 1) % 3 != 0:
                ans += cost[i]
        return ans
        """
        return sum([ c for i, c in enumerate(sorted(cost)[::-1]) if (i + 1) % 3 != 0 ])