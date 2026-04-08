# My intial solution (optimal solution)
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # [5,1,1,1], k = 0
        # calculate for those in front, calculate for those behind and calc myself
        count = 0
        for t in range(len(tickets)):
            tt, tk = tickets[t], tickets[k]
            if t <= k:
                count += min(tk, tt)
            else:
                count += tk - 1 if tt >= tk else tt
        return count

# For the sake of the queues lesson
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # solving using queues simulation
        queue = deque([(i, t) for i, t in enumerate(tickets)]) # tuple of idx, and cur val
        count = 0
        while queue:
            idx, val = queue.popleft()
            count +=1
            val -=1

            if idx == k and val == 0:
                return count
            elif val != 0:
                queue.append((idx, val))
