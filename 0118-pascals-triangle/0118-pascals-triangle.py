class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        elif numRows >= 3:
            ans = [[1],[1,1]]
            for i in range(numRows - 2):
                temp = list()
                for j in range(len(ans[-1]) - 1):
                    temp.append(ans[-1][j] + ans[-1][j + 1])
                ans.append([1, *temp, 1])
            return ans
        """
        if numRows >= 3:
            ans = [[1],[1,1]]
            for i in range(numRows - 2):
                temp = list()
                for j in range(len(ans[-1]) - 1):
                    temp.append(ans[-1][j] + ans[-1][j + 1])
                ans.append([1, *temp, 1])
            return ans
        else:
            return [[1]] if numRows == 1 else [[1],[1,1]]