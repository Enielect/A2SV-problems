class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ROWS, COLS = len(mat), len(mat[0])

        row = col = 0
        res = []

        for _ in range(ROWS * COLS):
            res.append(mat[row][col])

            if (row + col) % 2 == 0:
                if col == COLS - 1:
                    row +=1
                elif row == 0:
                    col +=1
                else:
                    col +=1
                    row -=1
            else:
                if row == ROWS - 1:
                    col +=1
                elif col == 0:
                    row +=1
                else:
                    row +=1
                    col -=1
        return res
