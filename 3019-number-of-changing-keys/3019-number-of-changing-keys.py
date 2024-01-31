class Solution:
    def countKeyChanges(self, s: str) -> int:
        return sum([1 for idx in range(len(s) - 1) if s[idx].lower() != s[idx + 1].lower()  ])