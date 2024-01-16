class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        ans = 0
        r_pos = [-1,-1]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'R':
                    r_pos = [i,j]
                    break
        
        for j in range(r_pos[-1] - 1, -1, -1):
            if board[r_pos[0]][j] == 'B':
                break
            elif board[r_pos[0]][j] == 'p':
                ans += 1
                break
        for j in range(r_pos[-1] + 1, 8):
            if board[r_pos[0]][j] == 'B':
                break
            elif board[r_pos[0]][j] == 'p':
                ans += 1
                break
        
        for j in range(r_pos[0] - 1,-1, -1):
            if board[j][r_pos[1]] == 'B':
                break
            elif board[j][r_pos[1]] == 'p':
                ans += 1
                break
        for j in range(r_pos[0] + 1, 8):
            if board[j][r_pos[1]] == 'B':
                break
            elif board[j][r_pos[1]] == 'p':
                ans += 1
                break
        return ans