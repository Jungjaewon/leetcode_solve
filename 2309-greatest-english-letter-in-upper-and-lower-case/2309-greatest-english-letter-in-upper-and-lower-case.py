class Solution:
    def greatestLetter(self, s: str) -> str:
        """
        ans = list()
        u_set, l_set = set(), set()
        for c in s:
            if c.isupper():
                u_set.add(c)
            else:
                l_set.add(c)
        for uc in u_set:
            if uc.lower() in l_set:
                ans.append(uc)
        if len(ans) > 1:
            ans = sorted(ans)
        return "" if len(ans) == 0 else f'{ans[-1]}'
        """
        """
        ans = list()
        u_set, l_set = set(), set()
        for c in s:
            if c.isupper():
                u_set.add(c)
            else:
                l_set.add(c)
        for uc in u_set:
            if uc.lower() in l_set:
                ans.append(uc)
        return "" if len(ans) == 0 else f'{sorted(ans)[-1]}'
        """
        u_set, l_set = set(), set()
        for c in s:
            if c.isupper():
                u_set.add(c)
            else:
                l_set.add(c)
        ans = [uc for uc in u_set if uc.lower() in l_set]
        if len(ans) > 1:
            ans = sorted(ans)
        return "" if len(ans) == 0 else f'{ans[-1]}'