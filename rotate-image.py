class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        COLS = len(matrix[0])
        ROWS = len(matrix)

        for r in  range(ROWS):
          # pretty neat way of choosing only the upper-right side of the matrix
            for c  in range (r+1, COLS):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
            matrix[r].reverse()
