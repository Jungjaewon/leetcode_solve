class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for idx in range(len(points) - 1):
            fx, fy = points[idx]
            sx, sy = points[idx + 1]
            dx = sx - fx
            dy = sy - fy
            if dx == dy:
                ans += abs(dx)
            elif dx > 0 and dy < 0:
                base_v = min([abs(dx), abs(dy)])
                ans += base_v
                dx -= base_v
                dy += base_v
                ans += (abs(dx) + abs(dy))
            elif dx < 0 and dy > 0:
                base_v = min([abs(dx), abs(dy)])
                ans += base_v
                dx += base_v
                dy -= base_v
                ans += (abs(dx) + abs(dy))
            elif dx > 0 and dy > 0:
                min_v = min([dx, dy]) 
                ans += min_v
                dx -= min_v
                dy -= min_v
                ans += (dx + dy)
            elif dx < 0 and dy < 0:
                max_v = max([dx, dy])
                ans += abs(max_v)
                dx -= max_v
                dy -= max_v
                ans += abs(dx + dy)
            elif dx != 0 and dy == 0:
                ans += abs(dx)
            elif dx == 0 and dy != 0:
                ans += abs(dy)
        return ans