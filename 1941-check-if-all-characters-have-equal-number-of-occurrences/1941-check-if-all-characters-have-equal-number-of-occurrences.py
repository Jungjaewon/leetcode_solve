class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        """
        a_dict = defaultdict(int)
        for c in s:
            a_dict[c] += 1
        a_list = [value for _, value in a_dict.items()]
        for i in range(1, len(a_list)):
            if a_list[i] != a_list[0]:
                return False
        return True
        """
        a_dict = dict(Counter(s))
        a_list = [value for _, value in a_dict.items()]
        for i in range(1, len(a_list)):
            if a_list[i] != a_list[0]:
                return False
        return True