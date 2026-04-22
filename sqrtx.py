class Solution:
    def mySqrt(self, x: int) -> int:
        l, h = 0, x
        res = x
        while l <= h:
            m = (l + h) // 2
            if m * m == x:
                return m
            elif m * m < x:
                res = m
                l = m + 1
            else:
                h = m - 1
        return res
