class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        """
        ans = list()
        for n in nums:
            ans.append([n, abs(n - 0)])
        ans.sort(key=lambda x : (x[1],-x[0]))
        return ans[0][0]
        """
        dist, ans = 10e6,-10e6
        for n in nums:
            d = abs(n - 0)
            print(f'd :{d}')
            if d < dist:
                dist, ans = d, n
            elif d == dist:
                if ans < n:
                    ans = n
        return ans
                    
            