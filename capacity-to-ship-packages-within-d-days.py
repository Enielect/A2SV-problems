class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # at the rate that we are currently check how many days it would take
        low, high = max(weights), sum(weights)

        res = sum(weights)
        while low <= high:
            mid = (low + high) // 2
            calc_days = 1
            cur_sum = mid

            for w in weights:
                if cur_sum - w < 0:
                    calc_days +=1
                    cur_sum = mid
                cur_sum -=w

            if calc_days <= days:
                high = mid - 1
                res = min(mid, res)
            else:
                low = mid + 1
        return res
