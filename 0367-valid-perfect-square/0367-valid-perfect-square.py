class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        s = int(sqrt(num))
        return s * s == num
        """
        #return int(sqrt(num)) * int(sqrt(num)) == num
        """
        #Ref : https://leetcode.com/problems/valid-perfect-square/discuss/3666963/PerfectSquare-oror-Best-Solution-oror-With-Explanation-oror-Intuition-%2B-Approach-%2B-Code
        i = 0
        while i * i < num:
            i += 1
        return i * i == num
        """
        # Ref https://leetcode.com/problems/valid-perfect-square/discuss/3285735/Beginner-friendly-in-python
        if num == 1:
            return True
        else:
            l,r = 0, num
            while l < r:
                mid = (l + r) // 2
                if mid * mid == num:
                    return True
                elif mid * mid > num:
                    r = mid
                else:
                    l = mid + 1
            return False
        
        