class NumMatrix:

    def __init__(self, matrix):
        # building a 2-d prefix array
        # to get the prefix at a particular cell = (cur + prf_above + prf_left - prf_top_left)
        m, n = len(matrix), len(matrix[0])
        self.sum = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(m):
            for c in range(n):
                self.sum[r + 1][c + 1] = matrix[r][c] + self.sum[r][c + 1] + self.sum[r + 1][c] - self.sum[r][c]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sum[row2+1][col2+1] - self.sum[row1][col2+1] - self.sum[row2+1][col1] + self.sum[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
