class Solution:
    def judgeCircle(self, moves):
        if len(moves) is 0:
            return True
        
        dirs = ['U', 'D', 'L', 'R']
        deltas = [[-1, 0], [+1, 0], [0, -1], [0, +1]]
        row = 0
        col = 0
        for move in moves:
            [drow, dcol] = deltas[dirs.index(move)]
            row += drow
            col += dcol

        return row == 0 and col == 0:
