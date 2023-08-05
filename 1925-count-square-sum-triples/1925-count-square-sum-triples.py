class Solution:
    def countTriples(self, n: int) -> int:
        """
        https://leetcode.com/problems/count-square-sum-triples/discuss/2677699/pythonororeasy
        x=0
			for i in range(1,n-1):
				for j in range(i+1,n):
					tri=math.sqrt((i**2+j**2))
					if tri<=n and int(tri)==tri :
						x+=2
			return x
        """
        ans = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c = sqrt(a * a + b * b)
                if c <= n and int(c) == c:
                    ans += 1
        return ans