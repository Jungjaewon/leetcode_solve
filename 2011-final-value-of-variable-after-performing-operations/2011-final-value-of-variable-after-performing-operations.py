class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        """
        ans = 0
        for op in operations:
            if '-' in op:
                ans -= 1
            else:
                ans += 1
        return ans
        """
        """
        ans = 0
        for op in operations:
            ans = ans + 1 if '+' in op else ans - 1
        return ans
        """
        return sum([1 if '+' in op else -1 for op in operations])