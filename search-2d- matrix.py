class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, h = 0, len(matrix) - 1
        while l <= h:
            m = (l + h) // 2
            cur = matrix[m]
            if cur[0] > target:
                h = m - 1
            elif cur[-1] < target:
                l = m + 1
            else:
                l, h = 0, len(cur) - 1
                while l <= h:
                    m = (l+h) // 2
                    if cur[m] == target:
                        return True
                    elif cur[m] < target:
                        l = m+1
                    else:
                        h = m - 1
                return False
        return False
