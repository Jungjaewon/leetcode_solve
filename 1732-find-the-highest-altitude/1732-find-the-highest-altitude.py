class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        """
        #gain.insert(0,0)
        ans = [0]
        for i in range(len(gain)):
            ans.append(ans[-1] + gain[i])
        return max(ans)
        """
        ans,t = 0,0
        for i in range(len(gain)):
            t = t + gain[i]
            ans = max(ans, t)
            
        return ans
        