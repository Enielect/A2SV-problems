class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        queue = deque()
        res = []
        for r in range(len(nums)):
            while queue and queue[-1][0] < nums[r]:
                queue.pop()
            queue.append((nums[r], r))

            if r >= k - 1:
                val, i = queue[0]
                res.append(val)
                if i == l:
                    queue.popleft()
                l +=1
        return res

