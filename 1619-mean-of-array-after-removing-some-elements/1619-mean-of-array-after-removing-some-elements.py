class Solution:
    def trimMean(self, arr: List[int]) -> float:
        cut = int(len(arr) * 0.05)
        arr = sorted(arr)
        for _ in range(cut):
            del arr[0]
        for _ in range(cut):
            del arr[-1]
        return sum(arr) / len(arr)
        