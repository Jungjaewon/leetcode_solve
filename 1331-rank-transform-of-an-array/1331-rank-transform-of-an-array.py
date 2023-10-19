class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        """
        rank_dict = { n: (i + 1) for i, n in enumerate(sorted(list(set(arr))))}
        ans = list()
        for n in arr:
            ans.append(rank_dict[n])
        return ans
        """
        rank_dict = { n: (i + 1) for i, n in enumerate(sorted(list(set(arr))))}
        return [ rank_dict[n] for n in arr]
        