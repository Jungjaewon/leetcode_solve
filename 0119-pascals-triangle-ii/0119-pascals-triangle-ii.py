class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            ans = [[1], [1,1]]
            for i in range(1, rowIndex):
                temp_l = list()
                temp_l.append(1)
                for j in range(len(ans[-1]) -1):
                    temp_l.append(ans[-1][j] + ans[-1][j + 1])
                temp_l.append(1)
                ans.append(temp_l)
            return ans[-1]