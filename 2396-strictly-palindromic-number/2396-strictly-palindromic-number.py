class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        return False
        """
        def numberToBase(n, b):
            if n == 0:
                return '0'
            digits = []
            while n:
                digits.append(int(n % b))
                n //= b
            return ''.join([str(x) for x in digits[::-1]])
        for b in range(2, n - 2 + 1):
            s_n = numberToBase(n, b)
            if s_n != s_n[::-1]:
                return False
        return True
        """
        #https://stackoverflow.com/questions/2267362/how-to-convert-an-integer-to-a-string-in-any-base