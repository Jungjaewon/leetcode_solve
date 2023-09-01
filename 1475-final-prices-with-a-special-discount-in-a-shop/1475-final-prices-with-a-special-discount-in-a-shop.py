class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        """
        ans = list()
        for idx, p in enumerate(prices):
            if idx + 1 == len(prices):
                ans.append(p)
            else:
                dis = None
                for n in prices[idx + 1:]:
                    if p >= n:
                        dis = n
                        break
                ans.append(p - dis if dis is not None else p)
        return ans
        """
        """
        ans = list()
        for idx, p in enumerate(prices):
            if idx + 1 == len(prices):
                ans.append(p)
            else:
                dis = None
                for n in range(idx + 1, len(prices)):
                    if p >= prices[n]:
                        dis = prices[n]
                        break
                ans.append(p - dis if dis is not None else p)
        return ans
        """
        """
        ans = list()
        for idx, p in enumerate(prices):
            dis = None
            for n in range(idx + 1, len(prices)):
                if p >= prices[n]:
                    dis = prices[n]
                    break
            ans.append(p - dis if dis is not None else p)
        return ans
        """
        # https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/discuss/685578/Python-31-pass-O(n)-code-using-stack-w-brief-explanation-and-analysis.
        res, stack = prices[:], []
        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                res[stack.pop()] -= price
            stack.append(i)
        return res
    