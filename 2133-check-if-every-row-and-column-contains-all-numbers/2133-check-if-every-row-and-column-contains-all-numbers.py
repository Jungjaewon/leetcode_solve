class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        print(f'n : {n}')
        ref_list = list(range(1, n + 1))
        for row in matrix:
            if sorted(row) != ref_list:
                return False
        for col in zip(*matrix):
            if sorted(col) != ref_list:
                return False
        
        
        return True