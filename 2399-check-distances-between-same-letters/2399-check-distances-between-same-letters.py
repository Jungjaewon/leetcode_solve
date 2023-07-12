class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        data_dict = defaultdict(list)
        for idx, c in enumerate(s):
            data_dict[c].append(idx)
        for c in data_dict:
            idx_list = sorted(data_dict[c])
            d = idx_list[-1] - idx_list[0] - 1
            if distance[ord(c) - ord('a')] != d:
                return False
        return True