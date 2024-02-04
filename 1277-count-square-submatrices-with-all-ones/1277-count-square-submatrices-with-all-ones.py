class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        """
        m,n,ans = len(matrix), len(matrix[0]),0
        for i in range(1, min(m,n) + 1):
            for j in range(len(matrix)):
                for k in range(len(matrix[j])):
                    temp = matrix[j : j + i]
                    for p in range(len(temp)):
                        temp[p] = temp[p][k : k + i]
                    ele_list = list(chain(*temp))
                    if len(ele_list) == (i * i) and all(ele_list):
                        ans += 1
            
        return ans
        """
        # https://leetcode.com/problems/count-square-submatrices-with-all-ones/discuss/3964606/Superb-Logic-Python3-greaterDP
        row=len(matrix)
        col=len(matrix[0])
        dp=[[0]*col for i in range(row)]
        for i in range(row):
            for j in range(col):
                if (i==0 or j==0) and matrix[i][j]==1:
                    dp[i][j]=1
        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][j]==1:
                    dp[i][j]=1+min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
        ans=0
        for rows in dp:
            ans+=sum(rows)
        return ans
            