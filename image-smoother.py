class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(img), len(img[0])
        smoothed_img = [[0] * COLS for _ in range(ROWS)]
        for row in range(ROWS):
            for col in range(COLS):
                smoothed_img[row][col] = self.calculate(row, col, COLS, ROWS, img)

        return smoothed_img
    
    def calculate(self, i, j, width, height, img):
        col_start, row_start = j - 1, i - 1
        res, size = 0, 0
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                if i >= 0 and i < height and j >=0 and j < width:
                    res += img[i][j]
                    size += 1
        return res // size
