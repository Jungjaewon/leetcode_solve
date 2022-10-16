class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        digits[len(digits) - 1] += 1
        flag = False
        
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 10:
                digits[i] = 0
                if i != 0:
                    digits[i - 1] += 1
                else:
                    flag = True
        if flag:
            return [1, *digits]
        else:
            return digits
                    