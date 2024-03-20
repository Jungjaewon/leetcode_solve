class Solution:
    def countPoints(self, rings: str) -> int:
        d_dict = defaultdict(set)
        for i in range(0, len(rings), 2):
            d_dict[rings[i + 1]].add(rings[i])
        return len([ 1 for x in d_dict if len(d_dict[x]) == 3])
        