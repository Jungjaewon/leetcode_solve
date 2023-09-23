class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = list()
        if n & 1 == 0:
            for i in range(1, n // 2 + 1):
                ans.append(i)
                ans.append(-i)
        else:
            for i in range(1, n // 2 + 1):
                ans.append(i)
                ans.append(-i)
            ans.append(0)
        return ans