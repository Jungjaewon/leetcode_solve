class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        a_l = [ int(w) for w in s.split() if w.isdigit()]
        return a_l == sorted(a_l) if len(set(a_l)) != 1 and not len(set(a_l)) < len(a_l) else False