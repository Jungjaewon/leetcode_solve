class Solution:
    def reverseString(self, s: List[str]) -> None:
        for idx in range(len(s) -1 ,-1, -1):
            s.append(s[idx])
        for _ in range(len(s) // 2):
            s.pop(0)
        """
        Do not return anything, modify s in-place instead.
        """
        