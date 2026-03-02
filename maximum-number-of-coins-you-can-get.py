class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        maxi, n = 0, len(piles)

        for i in range(n - 2, (n // 3) - 1, -2):
            maxi += piles[i]
        return maxi
