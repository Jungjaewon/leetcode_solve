class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        """
        pos, ans = list(), 0
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                if mat[x][y] == 1:
                    pos.append([x,y])
        def check(x,y, m, n):
            cnt = 0
            for i in range(n):
                if mat[x][i] == 1:
                    cnt += 1
            if cnt != 1:
                return False
            cnt = 0
            for i in range(m):
                if mat[i][y] == 1:
                    cnt += 1
            if cnt != 1:
                return False
            return True
        for x,y in pos:
            if check(x,y, len(mat), len(mat[0])):
                ans +=1
        return ans
        """
        pos, ans = set(), 0
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                if mat[x][y] == 1:
                    pos.add((x,y))
        def check(x,y, m, n):
            cnt = 0
            for i in range(n):
                if mat[x][i] == 1:
                    cnt += 1
            if cnt != 1:
                return False
            cnt = 0
            for i in range(m):
                if mat[i][y] == 1:
                    cnt += 1
            if cnt != 1:
                return False
            return True
        for x,y in pos:
            if check(x,y, len(mat), len(mat[0])):
                ans +=1
        return ans
        
            