class Solution:
    def isThree(self, n: int) -> bool:
        """
        cnt = sum([1 for i in range(1, n + 1) if n % i == 0])
        return True if cnt == 3 else False
        """
        #return True if sum([1 for i in range(1, n + 1) if n % i == 0]) == 3 else False
        #return True if len([1 for i in range(1, n + 1) if n % i == 0]) == 3 else False
        return sum([1 for i in range(1, n + 1) if n % i == 0]) == 3