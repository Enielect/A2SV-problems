class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # just remember that the initial transformation that we need is:
        # dx, dy = -dy, dx
        res = []
        rows, cols = len(matrix), len(matrix[0])

        row, col = 0, 0
        dx, dy = 1, 0

        for _ in range(rows * cols):
            res.append(matrix[row][col])
            matrix[row][col] = '.'

            if not (0 <= row + dy < rows and 0 <= col + dx < cols) or matrix[row + dy][col + dx] == '.':
                dx, dy = -dy, dx
            row, col = row + dy, col + dx
               
        return res
