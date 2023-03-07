class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        print(sorted(heights))
        return sum([1 if x != y else 0 for x,y in zip(heights, sorted(heights))])