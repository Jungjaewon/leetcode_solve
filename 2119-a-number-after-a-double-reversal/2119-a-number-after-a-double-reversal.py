class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        #return num == int(str(int(str(num)[::-1]))[::-1])
        if str(num) == '0':
            return True
        elif str(num)[-1] == '0':
            return False
        else:
            return True