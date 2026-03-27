class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        total, l, r = 0, 0, n - 1

        while l <= r:
            if l == r:
                return total + 1

            range_sum = people[l] + people[r]
            total +=1
            if range_sum > limit:
                r -=1
            else:
                l +=1
                r -=1
        return total
