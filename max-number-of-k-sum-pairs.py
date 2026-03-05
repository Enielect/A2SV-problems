class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        l, r, ops = 0, n - 1, 0
        ops = 0
        if n == 1 and nums[0] == k:
            return 1
        while l < r:
            cur_sum = nums[l] + nums[r]
            if cur_sum > k:
                r -=1
            elif cur_sum < k:
                l +=1
            else:
                ops +=1
                l, r = l + 1, r - 1
        return ops
