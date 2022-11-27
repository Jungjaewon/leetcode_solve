class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        return [x[0] for x in Counter(nums).most_common(k)]
        