class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        s = int(sqrt(num))
        return s * s == num
        """
        #return int(sqrt(num)) * int(sqrt(num)) == num
        """
        #Ref : https://leetcode.com/problems/valid-perfect-square/discuss/3666963/PerfectSquare-oror-Best-Solution-oror-With-Explanation-oror-Intuition-%2B-Approach-%2B-Code
        """
        i = 0
        while i * i < num:
            i += 1
        return i * i == num