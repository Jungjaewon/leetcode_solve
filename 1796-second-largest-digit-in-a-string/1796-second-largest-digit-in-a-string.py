class Solution:
    def secondHighest(self, s: str) -> int:
        digit_l = list({int(x) for x in s if x.isdigit()})
        if len(digit_l) <= 1:
            return -1
        else:
            return sorted(digit_l, reverse=True)[1]