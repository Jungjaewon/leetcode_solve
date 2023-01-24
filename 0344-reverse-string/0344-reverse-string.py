class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        for idx in range(len(s) -1 ,-1, -1):
            s.append(s[idx])
        for _ in range(len(s) // 2):
            s.pop(0)
        """
        s_i, e_i = 0, len(s) - 1
        while True:
            print(s_i, e_i)
            s[s_i], s[e_i] = s[e_i], s[s_i]
            
            if s_i == e_i:
                break
            elif len(s) & 1 == 0 and abs(s_i - e_i) == 1:
                break
            
            s_i, e_i = s_i + 1, e_i - 1
            
        """
        Do not return anything, modify s in-place instead.
        """
        