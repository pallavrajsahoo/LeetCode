class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = []
        for i in range(9):
            for j in range(9):
                current = board[i][j]
                if current != ".":
                    seen.extend([(i, current), (current, j), (i//3, j//3, current)])
        return len(seen) == len(set(seen))
            
        