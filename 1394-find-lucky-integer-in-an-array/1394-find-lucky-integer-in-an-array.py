class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c, ans = Counter(arr), list()
        for key in c:
            if c[key] == key:
                ans.append(key)
        return -1 if len(ans) == 0 else sorted(ans)[-1]