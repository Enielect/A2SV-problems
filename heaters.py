class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # for each house find the closet heater
        n = len(heaters)
        heaters.sort()

        ans = 0
        for house in houses:
            l, r = 0, n - 1
            closest = float('inf')
            while l <= r:
                m = (l + r) // 2
                closest = min(closest, abs(heaters[m] - house))

                if heaters[m] > house:
                    r = m - 1
                elif heaters[m] < house:
                    l = m + 1
                else:
                    break
            ans = max(ans, closest)
        return ans
