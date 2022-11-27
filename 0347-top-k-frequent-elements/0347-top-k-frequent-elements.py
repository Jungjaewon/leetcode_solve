class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        a_dict = defaultdict(int)
        for n in nums:
            a_dict[n] += 1
        return [x[0] for x in sorted(a_dict.items(), key=lambda x : x[1], reverse=True)[:k]]
        """
        from collections import Counter
        return [x[0] for x in Counter(nums).most_common(k)]
        """
        