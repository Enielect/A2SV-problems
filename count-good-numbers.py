class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        lower = n // 2
        upper = n - lower

        def exp(x, y):
            res = 1
            if y < 0:
                x, y = 1/x, -y
            
            while y > 0:
                if y % 2 == 1:
                    res = (res * x) % mod
                x = (x * x ) % mod
                y //= 2
            return res

        
        return (exp(5, upper) * exp(4, lower)) % mod

    