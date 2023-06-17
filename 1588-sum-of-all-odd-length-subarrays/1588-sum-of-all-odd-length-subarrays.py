class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        cnt,ans = 1, 0
        while cnt <= len(arr):
            idx = 0
            while idx < len(arr):
                if len(arr[idx : idx + cnt]) < cnt:
                    break
                ans += sum(arr[idx : idx + cnt])
                idx += 1
            cnt += 2
        return ans