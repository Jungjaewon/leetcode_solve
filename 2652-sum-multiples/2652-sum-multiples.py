class Solution:
    def sumOfMultiples(self, n: int) -> int:
        """
        ans = 0
        for num in range(1, n + 1):
            if num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
                ans += num
        return ans
        """
        # https://leetcode.com/problems/sum-multiples/discuss/3445711/Kotlin-O(1)-with-Diagram
        #return sum([num for num in range(1, n + 1) if num % 3 == 0 or num % 5 == 0 or num % 7 == 0])
        
        def count(value):
            low, high = value, n // value * value
            count = n // value
            return (low + high) * count // 2
        return count(3) + count(5) + count(7) - (count(15) + count(21) + count(35)) + count(105)