class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        #return num == int(str(int(str(num)[::-1]))[::-1])
        """
        if str(num) == '0':
            return True
        elif str(num)[-1] == '0':
            return False
        else:
            return True
        """
        """
        s_num = str(num)
        if s_num[-1] == '0' and len(s_num) > 1:
            return False
        else:
            return True
        """
        return False if str(num)[-1] == '0' and len(str(num)) > 1 else True
        
        