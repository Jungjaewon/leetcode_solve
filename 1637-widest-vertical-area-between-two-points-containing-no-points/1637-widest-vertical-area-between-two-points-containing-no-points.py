class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = sorted(points, key= lambda x : (x[0],x[1]))
        ans = -10e4
        for i in range(len(points) - 1):
            ans = max(ans, abs(points[i][0] - points[i + 1][0]))
        return ans
        
        