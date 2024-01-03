class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = -10e4
        for i in range(len(colors)):
            for j in range(len(colors)):
                if i == j:
                    continue
                else:
                    if colors[i] != colors[j]:
                        ans = max(ans, abs(i - j))
        return ans