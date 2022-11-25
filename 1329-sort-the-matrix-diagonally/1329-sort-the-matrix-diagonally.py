class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        #print(n,m)
        ans = [[0 for _ in range(m)] for _ in range(n)]
        
        coordinate = [[0, x] for x in range(m)]
        for x in range(n - 1):
            coordinate.append([0, x - n + 1])
        coordinate = [ [ [x + i, y + i] for i in range(n + 1)] for x, y in coordinate]
        #for xylist in coordinate:
        #    print(xylist)
        #print('*' * 15)
        for i in range(len(coordinate)):
            coordinate[i] = [[x,y] for x,y in coordinate[i] if -1 < x and x < n and -1 < y and y < m]
        #print(coordinate)
        #for xylist in coordinate:
        #    print(xylist)
        #print('*' * 15)
        for xylist in coordinate:
            temp_list = list()
            for x,y in xylist:
                temp_list.append(mat[x][y])
            temp_list.sort()
            #print(temp_list)
            for digit, xy in zip(temp_list, xylist):
                x, y = xy
                mat[x][y] = digit
        return mat
            
        
        