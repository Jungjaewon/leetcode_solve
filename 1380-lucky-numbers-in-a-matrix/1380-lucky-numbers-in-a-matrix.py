class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ans = list()
        t_matrix = list(zip(*matrix))
        for i in range(len(matrix)):
            row_max = min(matrix[i])
            for j in range(len(matrix[i])):
                v = matrix[i][j]
                col_max = max(t_matrix[j])
                if row_max == v and col_max == v:
                    ans.append(v)
        return ans