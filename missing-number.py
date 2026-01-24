class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        curr_sum, n, max_val = sum(nums), len(nums), max(nums)

        req_sum = n*(n + 1) // 2
        rem = req_sum - curr_sum

        if max_val + 1 == n:
            return max_val + 1
        return rem
