class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        if n == 1:
            return True
        elif n == 0 :
            return False
        else:
            while n != 1:
                if n % 2 != 0:
                    return False
                else:
                    n = n // 2
            return True
        """
        if n <= 0:
            return False
        
        power = round(math.log(n, 2))
        return 2 ** power == n
    #https://leetcode.com/problems/power-of-two/discuss/4260974/SOLVED-(ONE-LINER-!!!-)-BEATS-100-(FULLY-EXPLAINED)-%2B-SURPRISE-AT-END!
    #https://leetcode.com/problems/power-of-two/discuss/1638704/C%2B%2B-EASY-TO-SOLVE-oror-All-INTERVIEW-APPROACHES-with-Detailed-Explanations
                    