class Solution:
    def climbStairs(self, n: int) -> int:
        s_dict = {1: 1, 2: 2}
        for i in range(3, n + 1):
            s_dict[i] = s_dict[i - 1] + s_dict[i - 2]    
        return s_dict[n]