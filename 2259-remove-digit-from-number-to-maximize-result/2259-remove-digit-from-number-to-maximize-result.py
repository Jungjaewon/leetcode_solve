class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        idx_list = [idx for idx, c in enumerate(number) if c == digit]
        candidates = list()
        for idx in idx_list:
            temp = list(number)
            temp[idx] = ''
            candidates.append(''.join(temp))
        return str(max(candidates))