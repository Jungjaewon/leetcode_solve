class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ans = list()
        for idx, ab in enumerate(points):
            a,b = ab
            if x == a or y == b:
                ans.append([idx, abs(x - a) + abs(y - b)])
        return -1 if len(ans) == 0 else sorted(ans, key=lambda x : (x[1],x[0]))[0][0]
                