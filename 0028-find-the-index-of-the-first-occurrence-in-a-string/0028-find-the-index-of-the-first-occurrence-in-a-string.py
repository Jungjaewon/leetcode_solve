class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #return haystack.find(needle)
        for idx in range(len(haystack)):
            temp = haystack[idx:idx + len(needle)]
            if temp == needle:
                return idx
        return -1