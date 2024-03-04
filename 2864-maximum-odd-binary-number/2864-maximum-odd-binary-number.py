class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        one_cnt = len([1 for c in s if c == '1'])
        
        if one_cnt == 1:
            return '0' * (len(s) - 1) + '1'
        else:
            return '1' * (one_cnt - 1) + '0' * (len(s) - one_cnt) + '1'