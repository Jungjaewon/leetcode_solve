class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [True if x + extraCandies >= max(candies) else False for x in candies]