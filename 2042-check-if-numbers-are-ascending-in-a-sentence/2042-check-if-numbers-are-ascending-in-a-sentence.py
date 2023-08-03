class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        """
        a_l = [ int(w) for w in s.split() if w.isdigit()]
        return a_l == sorted(a_l) if len(set(a_l)) != 1 and not len(set(a_l)) < len(a_l) else False
        """
        """
        a_l = [ int(w) for w in s.split() if w.isdigit()]
        for idx, n in enumerate(a_l[:-1]):
            if not a_l[idx] < a_l[idx + 1]:
                return False
        return True
        """
        base = -1
        for idx, n in enumerate([int(w) for w in s.split() if w.isdigit()]):
            if not base < n:
                return False
            else:
                base = n
        return True