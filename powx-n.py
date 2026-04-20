
# recursive solutino
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0

        if n < 0:
            return self.myPow(1.0/x, -n)
        half = self.myPow(x, n//2)
        if n % 2 == 1:
            return half * half * x
        else:
            return half * half

#iterative solution:
class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if n < 0:
            n = -n
            x = 1.0 / x
        
        while n > 0:
            if n % 2 == 1:
                res *= x
            x = x * x
            n //= 2
        return res
