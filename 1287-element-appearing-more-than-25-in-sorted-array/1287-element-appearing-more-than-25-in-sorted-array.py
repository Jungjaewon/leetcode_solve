class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        for k,v in Counter(arr).items():
            if v / len(arr) > 0.25:
                return k