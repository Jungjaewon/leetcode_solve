class Solution:
    def repeatedCharacter(self, s: str) -> str:
        t_dict = defaultdict(int)
        for c in s:
            t_dict[c] += 1
            if t_dict[c] == 2:
                return c