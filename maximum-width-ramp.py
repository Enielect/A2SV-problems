class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        # keep a monotonic decreasing stack initially
        res = 0
        for j, num in enumerate(nums):
            while stack and nums[stack[-1]] <= num:
                res = max(res, j - stack.pop())
            stack.append(j)
        return res
