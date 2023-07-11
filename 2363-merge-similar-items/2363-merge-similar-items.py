class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        ans_dict = defaultdict(int)
        for n,w in items1 + items2:
            ans_dict[n] += w
        return [[key, ans_dict[key]] for key in sorted(ans_dict)]