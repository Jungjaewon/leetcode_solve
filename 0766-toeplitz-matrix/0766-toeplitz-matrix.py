class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m,n = len(matrix), len(matrix[0])
    
        for i in range(n):
            x,y = 0,i
            temp_l = list()
            while x < m and y < n:
                temp_l.append(matrix[x][y])
                y += 1
                x += 1
            t = temp_l[0]
            for j in range(1, len(temp_l)):
                if t != temp_l[j]:
                    return False
        for i in range(1, m):
            x,y = i,0
            temp_l = list()
            while x < m and y < n:
                temp_l.append(matrix[x][y])
                x += 1
                y += 1
            t = temp_l[0]
            for j in range(1, len(temp_l)):
                if t != temp_l[j]:
                    return False
        return True