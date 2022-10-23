class Solution:
    def climbStairs(self, n: int) -> int:
        s_dict = {1: 1, 2: 2, 3: 3, 4: 5, 5: 8}
        for i in range(6, 46):
            s_dict[i] = s_dict[i - 1] + s_dict[i - 2]
            
            if n in s_dict:
                return s_dict[n]