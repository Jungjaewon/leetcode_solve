class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        #two_ch = sum(sorted(prices)[:2])
        #return money if two_ch > money else money - two_ch
        return money if sum(sorted(prices)[:2]) > money else money - sum(sorted(prices)[:2])