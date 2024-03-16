class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/1735550/Python-Javascript-Easy-solution-with-very-clear-Explanation
        """
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit
        """
        #https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/4801758/2-Steps-Kadane's-Algorithm-or-Brute-Better-Optimal-or-Easy-Video-Explanation-in-Hindi
        n = len(prices)
        maxProfit = 0
        currMax_Profit = 0
        for i in range(1, n):
            currMax_Profit += prices[i] - prices[i-1]
            if currMax_Profit > 0:
                pass
            else:
                currMax_Profit = 0
            maxProfit = max(maxProfit, currMax_Profit)
        return maxProfit
                