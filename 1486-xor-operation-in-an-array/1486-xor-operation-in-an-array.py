class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr = [start + 2 * i for i in range(n)]
        ans = arr[0]
        for i in range(1, len(arr)):
            ans ^= arr[i]
        return ans