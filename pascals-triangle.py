class Solution:
    def generate(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        
        temp = self.generate(n - 1)

        res = [1] * n

        for i in range(1, n-1):
            res[i] = temp[-1][i-1] + temp[-1][i]
        temp.append(res)

        return temp
