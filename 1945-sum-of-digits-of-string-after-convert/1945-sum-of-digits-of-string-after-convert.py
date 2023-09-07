class Solution:
    def getLucky(self, s: str, k: int) -> int:
        temp_str = ''.join([ str(ord(c) - ord('a') + 1) for c in s])
        ans = 0
        while k:
            ans = sum([int(n) for n in temp_str])
            temp_str = str(ans)
            k -= 1 
        return ans
        
        