class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ans, temp = 0, 10e3
        while temp != 0:
            if num1 == 0 or num2 == 0:
                break
            if num1 >= num2:
                temp = num1 - num2
                num1 = temp
            else:
                temp = num2 - num1
                num2 = temp
            ans += 1
        return ans
                