class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # In each hour we can only take banana from one pile so max speeed in max(piles) per hour
        low, high = 1, max(piles)

        while low <= high:
            mid = (low + high) // 2
            # calculate the time number of hours we would use at mid rate\
            hrs = 0
            for p in piles:
                hrs += math.ceil(p / mid)
            if hrs <= h:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res
