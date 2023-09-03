class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        """
        ans = list()
        for idx, ab in enumerate(points):
            a,b = ab
            if x == a or y == b:
                ans.append([idx, abs(x - a) + abs(y - b)])
        return -1 if len(ans) == 0 else sorted(ans, key=lambda x : (x[1],x[0]))[0][0]
        """
        """
        a_idx, ans = -1, -1
        for idx, ab in enumerate(points):
            a,b = ab
            if x == a or y == b:
                dis = abs(x - a) + abs(y - b)
                if ans == -1:
                    a_idx, ans = idx, dis
                else:
                    if dis < ans:
                        a_idx, ans = idx, min(dis, ans)
                    elif dis == ans:
                        a_idx = min(idx, a_idx)
        return a_idx
        """
        points = [[idx, item] for idx, item in enumerate(points) if item[0] == x or item[1] == y]
        a_idx, ans = -1, -1
        for idx, ab in points:
            a,b = ab
            if x == a or y == b:
                dis = abs(x - a) + abs(y - b)
                if ans == -1:
                    a_idx, ans = idx, dis
                else:
                    if dis < ans:
                        a_idx, ans = idx, min(dis, ans)
                    elif dis == ans:
                        a_idx = min(idx, a_idx)
        return a_idx
                