class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
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