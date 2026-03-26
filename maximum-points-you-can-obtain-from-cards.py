class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # remove the smallest subarray with length n - k
        n = len(cardPoints)
        range_sum = 0
        for r in range(n - k):
            range_sum += cardPoints[r]
        min_sum = range_sum

        l = 0
        for r in range(n - k, n):
            range_sum += cardPoints[r]
            range_sum -= cardPoints[l]
            l +=1
            min_sum = min(min_sum, range_sum)
        return sum(cardPoints) - min_sum
