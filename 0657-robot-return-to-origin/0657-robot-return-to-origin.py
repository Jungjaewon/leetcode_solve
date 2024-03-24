class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x,y = 0, 0
        moves = moves.replace("LR", "").replace("RL", "").replace("UD", "").replace("DU", "")
        dir_dict = {'U' : [-1,0], 'D': [1,0], 'R' : [0,1], 'L' : [0,-1]}
        for c in moves:
            dx, dy = dir_dict[c][0],dir_dict[c][1]
            x, y = x + dx, y + dy
        return x == 0 and y == 0