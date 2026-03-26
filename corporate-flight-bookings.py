class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n + 1) # difference array
        for l, r, s in bookings:
            diff[l - 1] +=s
            if r < n:
                diff[r] -=s

        cur = 0
        res = [0] * n
        for d in range(n):
            res[d] = diff[d] + cur
            cur+=diff[d]
        return res
