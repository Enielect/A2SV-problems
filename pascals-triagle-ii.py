class Solution:
    def getRow(self, n: int) -> List[int]:
        if n == 0:
            return [1]

        prv = self.getRow(n-1)

        res = [1] * (n + 1)

        for i in range(1, n):
            res[i] = prv[i] + prv[i-1]
        return res
