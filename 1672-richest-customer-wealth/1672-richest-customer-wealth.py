class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(bank) for bank in accounts])
        