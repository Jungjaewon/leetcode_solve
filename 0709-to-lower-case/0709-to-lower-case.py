class Solution:
    def toLowerCase(self, s: str) -> str:
        #return s.lower()
        return "".join([ chr(ord(c) + 32) if 65 <= ord(c) and ord(c) <= 90 else c for c in s])