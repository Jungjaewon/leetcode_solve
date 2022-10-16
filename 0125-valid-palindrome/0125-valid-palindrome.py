class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([a.lower() for a in s if a.isalnum()])
        return s == s[::-1]
        