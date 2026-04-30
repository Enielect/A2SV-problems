class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, h = 1, max(nums)
        res = max(nums)
        while l <= h:
            m =(l+h)//2
            if sum(math.ceil(x / m) for x in nums) > threshold:
                l = m + 1
            else:
                res = m
                h = m -1
        return res
