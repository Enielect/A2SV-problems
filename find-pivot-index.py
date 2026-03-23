class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        psl = [0] * (n + 1)
        psr = [0] * (n + 1)
        for l in range(n):
            psl[l + 1] = nums[l] + psl[l]
        for r in range(n - 1, -1, -1):
            psr[r] = nums[r] + psr[r + 1]
        
        l, r = 0, n - 1
        psl = psl[1:]
        for i in range(len(psl)):
            if psl[i] == psr[i]:
                return i
        return -1
