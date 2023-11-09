class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m,n = len(img), len(img[0])
        ans = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n): 
                temp = []
                for x in range(i - 1, i + 1 + 1):
                    for y in range(j - 1, j + 1 + 1):
                        if -1 < x and x < m and -1 < y and y < n:
                            temp.append(img[x][y])
                ans[i][j] = math.floor(sum(temp) / float(len(temp)))
            
        return ans