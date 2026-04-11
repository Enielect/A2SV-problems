class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in range(2 * n):
            cur = nums[i % n]
            while stack and cur > stack[-1][1]:
                idx, val = stack.pop()
                if res[idx] == -1:
                    res[idx] = cur
            stack.append((i%n, cur))
        return res
