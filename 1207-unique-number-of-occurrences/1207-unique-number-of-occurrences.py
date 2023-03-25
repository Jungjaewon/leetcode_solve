class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        a_dict = defaultdict(int)
        for n in arr:
            a_dict[n] += 1
        return len(a_dict.values()) == len(set(a_dict.values()))