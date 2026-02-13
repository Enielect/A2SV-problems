class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(matrix), len(matrix[0])
        transpose = [[None]*ROWS for _ in range(COLS)]

        for row in range(ROWS):
            for col in range(COLS):
                transpose[col][row] = matrix[row][col]
        return transpose
