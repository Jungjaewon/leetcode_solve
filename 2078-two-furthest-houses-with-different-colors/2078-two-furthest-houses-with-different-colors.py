class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        """
        ans = -10e4
        for i in range(len(colors)):
            for j in range(len(colors)):
                if i == j:
                    continue
                else:
                    if colors[i] != colors[j]:
                        ans = max(ans, abs(i - j))
        return ans
        """
        """
        ans = -10e4
        for i in range(len(colors)):
            for j in range(i + 1, len(colors)):
                if colors[i] != colors[j]:
                    ans = max(ans, abs(i - j))
        return ans
        """
        i,j, ans = 0, len(colors) - 1, -10e4
        while i < j:
            if colors[i] != colors[j]:
                ans = max(ans, abs(i - j))
            i += 1
        i = 0
        while i < j:
            if colors[i] != colors[j]:
                ans = max(ans, abs(i - j))
            j -= 1
        return ans
        