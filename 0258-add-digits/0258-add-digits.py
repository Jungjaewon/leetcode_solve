class Solution:
    def addDigits(self, num: int) -> int:
        temp_list = [int(s) for s in str(num)]
        while len(temp_list) != 1:
            ret = sum(temp_list)
            temp_list = [int(s) for s in str(ret)]
        return sum(temp_list)