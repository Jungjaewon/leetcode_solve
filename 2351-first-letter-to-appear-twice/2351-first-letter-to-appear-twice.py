class Solution:
    def repeatedCharacter(self, s: str) -> str:
        """
        t_dict = defaultdict(int)
        for c in s:
            t_dict[c] += 1
            if t_dict[c] == 2:
                return c
        """
        """
        a_list = [0] * 26
        for c in s:
            a_list[ord(c) - ord('a')] += 1
            if a_list[ord(c) - ord('a')] == 2:
                return c
        """
        a_set = set()
        for c in s:
            if c in a_set:
                return c
            a_set.add(c)